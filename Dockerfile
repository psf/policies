FROM python:3.11.3-slim-bullseye as docs

RUN set -x \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential git libcairo2-dev libfreetype6-dev \
        libjpeg-dev libpng-dev libz-dev

RUN set -x \
    && python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:${PATH}"

RUN pip --no-cache-dir --disable-pip-version-check install \
    --upgrade pip setuptools wheel
COPY requirements.txt /tmp/requirements.txt
RUN set -x \
    && pip --no-cache-dir --disable-pip-version-check \
            install -r /tmp/requirements.txt \
    && pip check \
    && find /opt/venv -name '*.pyc' -delete

WORKDIR /opt/venv/src/
COPY mkdocs.yml /opt/venv/src/mkdocs.yml
COPY docs /opt/venv/src/docs
