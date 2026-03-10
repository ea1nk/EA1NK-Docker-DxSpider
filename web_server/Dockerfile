FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends git build-essential libmariadb-dev libev-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN git clone --depth 1 https://github.com/coulisse/spiderweb.git /opt/spiderweb \
    && cp /opt/spiderweb/cfg/config.json.template /opt/spiderweb/cfg/config.json

COPY web_server/patches/dxtelnet.py /opt/spiderweb/lib/dxtelnet.py
COPY web_server/patches/qry_builder.py /opt/spiderweb/lib/qry_builder.py
COPY web_server/patches/table.js /opt/spiderweb/static/js/dev/table.js
COPY web_server/patches/table.js /opt/spiderweb/static/js/rel/table.min.js
COPY web_server/patches/index.html /opt/spiderweb/templates/index.html

RUN pip install --no-cache-dir -r /opt/spiderweb/requirements.txt

WORKDIR /opt/spiderweb

COPY web_server/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]
