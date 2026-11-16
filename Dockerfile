FROM ghcr.io/astral-sh/uv:0.13.1@sha256:4a1f3666816dafadd20ceb71eac9a7d56d7ef30279f7d64048519ab901ada336 AS uv

FROM python:3.14.8-slim-bookworm AS docs

RUN set -x \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential git libcairo2-dev libfreetype6-dev \
        libjpeg-dev libpng-dev libz-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=uv /uv /bin/uv

ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

RUN uv venv /opt/venv
WORKDIR /opt/venv/src/
COPY pyproject.toml uv.lock .python-version /opt/venv/src/
RUN uv sync --locked --no-dev --no-cache

COPY mkdocs.yml /opt/venv/src/mkdocs.yml
COPY docs /opt/venv/src/docs
COPY hooks /opt/venv/src/hooks
