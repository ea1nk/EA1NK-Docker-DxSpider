# --- Etapa 1: compilación de dependencias Python ---
FROM python:3.13-slim AS builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends git build-essential libmariadb-dev libev-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/coulisse/spiderweb.git /opt/spiderweb \
    && rm -rf /opt/spiderweb/.git \
    && cp /opt/spiderweb/cfg/config.json.template /opt/spiderweb/cfg/config.json

RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -r /opt/spiderweb/requirements.txt

# --- Etapa 2: imagen final sin herramientas de compilación ---
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends libmariadb3 libev4 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /opt/spiderweb /opt/spiderweb

# Los parches van al final para que modificarlos no invalide la capa de pip
COPY web_server/patches/dxtelnet.py /opt/spiderweb/lib/dxtelnet.py
COPY web_server/patches/qry_builder.py /opt/spiderweb/lib/qry_builder.py
COPY web_server/patches/table.js /opt/spiderweb/static/js/dev/table.js
COPY web_server/patches/table.js /opt/spiderweb/static/js/rel/table.min.js
COPY web_server/patches/index.html /opt/spiderweb/templates/index.html

WORKDIR /opt/spiderweb

COPY --chmod=755 web_server/entrypoint.sh /entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]
