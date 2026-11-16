"""Publish pypi.org/policies.json from the front matter of PyPI policy pages.

PyPI reads this file to know the current revision of each policy, and
notifies users when a revision changes. A page is included only if its
front matter has a `revision`. A page's `subprocessors` list is also
rendered into the page itself.
"""

from __future__ import annotations

import datetime as dt
import html
import json
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Any

from mkdocs.exceptions import PluginError

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig
    from mkdocs.structure.files import Files
    from mkdocs.structure.pages import Page

SECTION = "pypi.org/"
AUDIENCES = {"users", "organizations"}
NOTICE_PERIOD = dt.timedelta(days=30)

_policies: dict[str, dict[str, Any]] = {}


def on_pre_build(config: MkDocsConfig) -> None:
    _policies.clear()


def on_page_content(output: str, page: Page, config: MkDocsConfig, files: Files) -> str:
    meta = page.meta
    if not page.file.src_uri.startswith(SECTION) or "revision" not in meta:
        return output

    name = page.file.src_uri
    slug = PurePosixPath(name).stem.lower()
    if slug in _policies:
        raise PluginError(f"{name}: another policy already uses the name {slug!r}")

    revision, effective = meta.get("revision"), meta.get("effective")
    if not isinstance(revision, dt.date) or not isinstance(effective, dt.date):
        raise PluginError(f"{name}: revision and effective must be YYYY-MM-DD dates")
    if meta.get("audience") not in AUDIENCES:
        raise PluginError(f"{name}: audience must be one of {sorted(AUDIENCES)}")
    if meta.get("require_acceptance") and meta["audience"] != "organizations":
        raise PluginError(f"{name}: only organizations can be asked to accept")

    retired = bool(meta.get("retired", False))
    notify = meta.get("notify", True) and not retired
    if notify:
        if not meta.get("summary"):
            raise PluginError(f"{name}: summary is required when notify is true")
        if effective - revision < NOTICE_PERIOD:
            raise PluginError(
                f"{name}: effective must be at least {NOTICE_PERIOD.days} days "
                "after revision"
            )

    policy: dict[str, Any] = {
        "title": page.title,
        # Relative to policies.json, so it works on any host.
        "url": page.url.removeprefix(SECTION),
        "audience": meta["audience"],
        "revision": revision.isoformat(),
        "effective": effective.isoformat(),
        "summary": meta.get("summary", ""),
        "description": meta.get("description", ""),
        "require_acceptance": bool(meta.get("require_acceptance", False)),
        "notify": bool(notify),
        "retired": retired,
    }
    if "subprocessors" in meta:
        policy["subprocessors"] = [
            {"name": s["name"], "category": s["category"], "purpose": s["purpose"]}
            for s in meta["subprocessors"]
        ]
    _policies[slug] = policy
    return output


def on_page_markdown(
    markdown: str, page: Page, config: MkDocsConfig, files: Files
) -> str:
    """Render a page's `subprocessors` front matter as one grouped table."""
    subprocessors = page.meta.get("subprocessors")
    if subprocessors is None:
        return markdown

    groups: dict[str, list[dict[str, Any]]] = {}
    for s in subprocessors:
        fields = ("name", "category", "purpose", "data")
        if not all(isinstance(s.get(key), str) for key in fields) or not s.get("terms"):
            raise PluginError(
                f"{page.file.src_uri}: each subprocessor needs a name, category, "
                "purpose, data and terms"
            )
        groups.setdefault(s["category"], []).append(s)

    e = html.escape
    rows: list[str] = []
    for category, members in groups.items():
        rows.append(f'<tr><th colspan="4" scope="colgroup">{e(category)}</th></tr>')
        for s in members:
            terms = "<br>".join(
                f'<a href="{e(t["url"])}">{e(t["title"])}</a>' for t in s["terms"]
            )
            rows.append(
                f'<tr><th scope="row">{e(s["name"])}</th><td>{e(s["purpose"])}</td>'
                f"<td>{e(s['data'])}</td><td>{terms}</td></tr>"
            )
    table = (
        '<div class="subprocessors">\n<table>\n<thead><tr><th>Provider</th>'
        "<th>Purpose</th><th>Personal data</th><th>Terms</th></tr></thead>\n<tbody>\n"
        + "\n".join(rows)
        + "\n</tbody>\n</table>\n</div>"
    )
    return f"{markdown}\n\n{table}\n"


def on_post_build(config: MkDocsConfig) -> None:
    path = Path(config["site_dir"]) / SECTION / "policies.json"
    path.write_text(json.dumps(_policies, indent=2, sort_keys=True))
