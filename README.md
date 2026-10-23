# Python Software Foundation Policies

This repository acts as the canonical source for the policies published by
the [Python Software Foundation](https://python.org/psf/).

## Development

You can use `make serve` to start a development server with live-reloading as you
edit documents. Run `make` to see the other targets, such as `make check`.

Once it has started, navigate to [http://localhost:10000](http://localhost:10000)
in your browser! Any edits made will render as you save your work.

### Adding new pages

To add a new page, you'll need to do two things:

1. Create the page itself in the appropriate location under [`./docs`](./docs/).
2. Add the page to the `nav` hierarchy in [`mkdocs.yml`](./mkdocs.yml).

### PyPI policies

Pages under `docs/pypi.org/` with a `revision` in their front matter are
published to `pypi.org/policies.json`. PyPI reads that file and emails users
when a revision changes.

```yaml
---
title: Data Processing Addendum
audience: organizations     # "users", or "organizations" for paid organizations
revision: 2026-11-01        # change this date only for a material change
effective: 2026-12-01       # at least 30 days after revision
summary: One sentence that goes in the email.
description: One sentence describing the document, for PyPI's Trust Center.
require_acceptance: true    # optional: owners must click "Accept" on PyPI
notify: false               # optional: record the revision without emailing anyone
---
```

Fixing a typo? Edit the text and leave `revision` alone. Nobody is notified.

Retiring a policy? Don't delete the page: add `retired: true` and move it under
"Superseded" in the nav. PyPI stops showing it, and the page stays readable.
If a page disappears from `policies.json` instead, PyPI treats it the same way
and reports it as a likely mistake.

The subprocessor list lives only in the front matter of
`docs/pypi.org/Subprocessors.md`; the page and PyPI's Trust Center both render it.
