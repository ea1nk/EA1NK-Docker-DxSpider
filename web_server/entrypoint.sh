#!/bin/sh
set -eu

cd /opt/spiderweb

mkdir -p data log cfg

python3 - <<'PY'
import json
import os
from pathlib import Path

config_path = Path('/opt/spiderweb/cfg/config.json')
if not config_path.exists():
    template_path = Path('/opt/spiderweb/cfg/config.json.template')
    config_path.write_text(template_path.read_text(), encoding='utf-8')

cfg = json.loads(config_path.read_text(encoding='utf-8'))

cfg.setdefault('mysql', {})
cfg['mysql']['host'] = os.getenv('SPIDERWEB_DB_HOST', cfg['mysql'].get('host', 'spider_database'))
cfg['mysql']['user'] = os.getenv('SPIDERWEB_DB_USER', cfg['mysql'].get('user', 'sysop'))
cfg['mysql']['passwd'] = os.getenv('SPIDERWEB_DB_PASS', cfg['mysql'].get('passwd', ''))
cfg['mysql']['db'] = os.getenv('SPIDERWEB_DB_NAME', cfg['mysql'].get('db', 'spiderdb'))

cfg['mycallsign'] = os.getenv('SPIDERWEB_MYCALLSIGN', cfg.get('mycallsign', 'EA1NK-8'))
cfg['mail'] = os.getenv('SPIDERWEB_MAIL', cfg.get('mail', 'sysop@example.com'))

cfg.setdefault('telnet', {})
cfg['telnet']['telnet_host'] = os.getenv('SPIDERWEB_TELNET_HOST', cfg['telnet'].get('telnet_host', 'dxspider-node'))
cfg['telnet']['telnet_port'] = str(os.getenv('SPIDERWEB_TELNET_PORT', cfg['telnet'].get('telnet_port', '7300')))
cfg['telnet']['telnet_user'] = os.getenv('SPIDERWEB_TELNET_USER', cfg['telnet'].get('telnet_user', 'EA1NK'))
cfg['telnet']['telnet_password'] = os.getenv('SPIDERWEB_TELNET_PASSWORD', cfg['telnet'].get('telnet_password', ''))

config_path.write_text(json.dumps(cfg, indent=2), encoding='utf-8')
PY

exec python3 wsgi.py
