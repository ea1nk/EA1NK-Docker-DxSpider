# 📂 EA1NK-Docker-DXSpider
### High-Performance DX Cluster Stack with WebUI, MariaDB & Nginx

[![Docker](https://img.shields.io/badge/Docker-24.0+-blue?logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-GPL--2.0-red.svg)](https://opensource.org/licenses/GPL-2.0)
[![Platform](https://img.shields.io/badge/Platform-Linux%20(amd64/arm64)-orange)](https://www.debian.org)

This repository provides a **Microservices Stack** designed to deploy a high-performance **DXSpider** node (Mojo branch), fully containerized and production-ready.

---

## 🏗️ Stack Architecture

The deployment consists of four main interconnected components running within an isolated internal network:

1.  **DXSpider Node (Mojo):** The core cluster engine, optimized for asynchronous processes and low latency.
2.  **MariaDB 10.11:** Relational database engine for persistent storage of users, spots, and node configuration.
3.  **WebUI (ttyd/Mojo Web):** A tactical web-based interface for remote administration and monitoring via browser.
4.  **NGINX Reverse Proxy:** Acts as a secure gateway, managing HTTP/Websocket traffic to the WebUI and providing an additional layer of protection.

