```
███████╗ ██████╗ ██████╗     ██████╗ ███████╗██╗   ██╗██╗ ██████╗███████╗███████╗
██╔════╝██╔════╝██╔═══██╗    ██╔══██╗██╔════╝██║   ██║██║██╔════╝██╔════╝██╔════╝
███████╗██║     ██║   ██║    ██║  ██║█████╗  ██║   ██║██║██║     █████╗  ███████╗
╚════██║██║     ██║▄▄ ██║    ██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║     ██╔══╝  ╚════██║
███████║╚██████╗╚██████╔╝    ██████╔╝███████╗ ╚████╔╝ ██║╚██████╗███████╗███████║
╚══════╝ ╚═════╝ ╚══▀▀═╝     ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝╚══════╝
                                                                                 
███████╗ █████╗  ██╗███╗   ██╗██╗  ██╗                                           
██╔════╝██╔══██╗███║████╗  ██║██║ ██╔╝                                           
█████╗  ███████║╚██║██╔██╗ ██║█████╔╝                                            
██╔══╝  ██╔══██║ ██║██║╚██╗██║██╔═██╗                                            
███████╗██║  ██║ ██║██║ ╚████║██║  ██╗           
2026 EA1NK-Docker-DXSpider High-Performance DX Cluster Stack with WebUI, MariaDB & Nginx
```
# 🐳 EA1NK-Docker-DXSpider 
### High-Performance DX Cluster Stack with WebUI, MariaDB & Nginx

[![Docker](https://img.shields.io/badge/Docker-24.0+-blue?logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-GPL--2.0-red.svg)](https://opensource.org/licenses/GPL-2.0)
[![Platform](https://img.shields.io/badge/Platform-Linux%20(amd64/arm64)-orange)](https://www.debian.org)

This repository provides a **Microservices Stack** designed to deploy a high-performance **DXSpider** node (Mojo branch), fully containerized and production-ready.

---

## 🏗️ Stack Architecture & Credits

This project is **heavily based** on the excellent work by **9M2PJU** in his [9M2PJU-DXSpider-Docker](https://github.com/9M2PJU/dxspider.git) repository. It has been customized, optimized for Alpine 3.20, and expanded to include a full MariaDB/Nginx stack.

The web interface is powered by **[Spiderweb](https://github.com/coulisse/spiderweb/)**, an open-source DX Cluster web frontend developed by **IU1BOW - Corrado Gerbaldo**.

This project applies local patches to the Spiderweb interface during the image build process from the files stored in `web_server/patches/`. These patches are used to adapt Spiderweb behavior and presentation to this stack when needed.

The deployment consists of four main interconnected components running within an isolated internal network:

1.  **DXSpider Node (Mojo):** The core cluster engine, optimized for asynchronous processes and low latency.
2.  **MariaDB 10.11:** Relational database engine for persistent storage of users, spots, and node configuration.
3.  **Spiderweb (IU1BOW):** A feature-rich web frontend for DX Cluster, displaying live spots, statistics, charts and propagation data. Developed by [IU1BOW - Corrado Gerbaldo](https://github.com/coulisse/spiderweb/).
4.  **WebUI (ttyd/Mojo Web):** A tactical web-based interface for remote sysop administration and monitoring via browser.
5.  **NGINX Reverse Proxy:** Acts as a secure gateway, managing HTTP/Websocket traffic to the WebUI and providing an additional layer of protection.

---

## 🚀 Quick Start Guide

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) 24.0+
- [Docker Compose](https://docs.docker.com/compose/) v2
- A valid amateur radio callsign

### 1. Clone the repository

```bash
git clone https://github.com/ea1nk/EA1NK-Docker-DxSpider.git
cd EA1NK-Docker-DxSpider
```

### 2. Configure your `.env` file

Copy or edit the `.env` file and fill in your details:

```env
# Your cluster callsign (e.g. EA1NK-8)
CLUSTER_CALLSIGN=MYCALL-8

# Sysop details
CLUSTER_SYSOP_NAME=YourName
CLUSTER_SYSOP_CALLSIGN=MYCALL
CLUSTER_SYSOP_PASSWORD=your_sysop_password

# Location
CLUSTER_LATITUDE=40.41650
CLUSTER_LONGITUDE=-3.70357
CLUSTER_LOCATOR=IN80DO
CLUSTER_QTH=Madrid, Spain

# Contact
CLUSTER_SYSOP_EMAIL=you@example.com

# Hostname (used in telnet banner)
CLUSTER_DX_HOSTNAME=dx.yourdomain.com
CLUSTER_PORT=7300
CLUSTER_SYSOP_PORT=8050

# MariaDB — change these before first run
CLUSTER_DB_USER=sysop
CLUSTER_DB_PASS=change_me
CLUSTER_DB_ROOT_PASSWORD=change_me_root
CLUSTER_DB_NAME=spiderdb

# Spiderweb internal telnet user (auto-created)
CLUSTER_SPIDERWEB_USER=SPIDERWEBUSER
CLUSTER_SPIDERWEB_PASSWORD=change_me_web
```

> **Note:** `CLUSTER_SPIDERWEB_USER` and `CLUSTER_SPIDERWEB_PASSWORD` are created automatically in DXSpider at startup — you don't need to create them manually.

### 3. Build and start the stack

```bash
docker compose up -d --build
```

The first run will build the DXSpider and Spiderweb images. This may take a few minutes.

### 4. Check that everything is running

```bash
docker compose ps
```

All four services should show `Up` or `Up (healthy)`.

### 5. Access the web interface

| Service | URL |
|---|---|
| Spiderweb (DX spots & stats) | http://localhost/ |
| Sysop console (ttyd) | http://localhost/console |
| Telnet cluster access | `telnet localhost 7300` |

### 6. Stopping and restarting

```bash
# Stop
docker compose down

# Start again (no rebuild needed)
docker compose up -d
```

> **Data persistence:** All spot data and user configuration is stored in `./database_data/` (MariaDB volume) and `./local_data/` (DXSpider config). These directories are excluded from git.


