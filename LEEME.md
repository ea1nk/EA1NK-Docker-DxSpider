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
2026 EA1NK-Docker-DXSpider Stack DX Cluster de alto rendimiento con WebUI, MariaDB y Nginx
```
# 🐳 EA1NK-Docker-DXSpider
### Stack DX Cluster de alto rendimiento con WebUI, MariaDB y Nginx

[![Docker](https://img.shields.io/badge/Docker-24.0+-blue?logo=docker)](https://www.docker.com/)
[![Licencia](https://img.shields.io/badge/License-GPL--3.0-red.svg)](https://opensource.org/licenses/GPL-3.0)
[![Plataforma](https://img.shields.io/badge/Platform-Linux%20(amd64/arm64)-orange)](https://www.debian.org)

Este repositorio ofrece un **stack de microservicios** para desplegar un nodo **DXSpider** (rama Mojo) totalmente contenedorizado y listo para producción.

---

## Arquitectura del stack y creditos

Este proyecto esta **fuertemente basado** en el excelente trabajo de **9M2PJU** en su repositorio [9M2PJU-DXSpider-Docker](https://github.com/9M2PJU/dxspider.git). Se ha personalizado, optimizado para Alpine 3.20 y ampliado con un stack completo MariaDB/Nginx.

La interfaz web esta impulsada por **[Spiderweb](https://github.com/coulisse/spiderweb/)**, un frontend web de DX Cluster de codigo abierto desarrollado por **IU1BOW - Corrado Gerbaldo**.

Este proyecto aplica parches locales sobre la interfaz Spiderweb durante la construccion de la imagen, a partir de los ficheros almacenados en `web_server/patches/`. Estos parches se usan cuando hace falta adaptar el comportamiento o la presentacion de Spiderweb a este stack.

El despliegue se compone de cinco servicios principales interconectados dentro de una red interna aislada:

1. **DXSpider Node (Mojo):** Motor principal del cluster, optimizado para procesos asincronos y baja latencia.
2. **MariaDB 10.11:** Motor de base de datos relacional para almacenamiento persistente de spots.
3. **Spiderweb (IU1BOW):** Frontend web para DX Cluster con spots en vivo, estadisticas, graficas y datos de propagacion.
4. **WebUI (ttyd/Mojo Web):** Interfaz web para administracion remota del sysop desde navegador.
5. **Nginx Reverse Proxy:** Pasarela de entrada para trafico HTTP/WebSocket hacia las interfaces web.

---

## Guia rapida de inicio

### Requisitos previos

- [Docker](https://docs.docker.com/get-docker/) 24.0+
- [Docker Compose](https://docs.docker.com/compose/) v2
- Un indicativo de radioaficionado valido

### 1. Clonar el repositorio

```bash
git clone https://github.com/ea1nk/EA1NK-Docker-DxSpider.git
cd EA1NK-Docker-DxSpider
```

### 2. Configurar el archivo `.env`

Edita el archivo `.env` y rellena tus datos:

```env
# Indicativo del cluster (ejemplo: EA1NK-8)
CLUSTER_CALLSIGN=MYCALL-8

# Datos del sysop
CLUSTER_SYSOP_NAME=TuNombre
CLUSTER_SYSOP_CALLSIGN=MYCALL
CLUSTER_SYSOP_PASSWORD=tu_password_sysop

# Ubicacion
CLUSTER_LATITUDE=40.41650
CLUSTER_LONGITUDE=-3.70357
CLUSTER_LOCATOR=IN80DO
CLUSTER_QTH=Madrid, Spain

# Contacto
CLUSTER_SYSOP_EMAIL=tu@email.com

# Hostname (aparece en banner telnet)
CLUSTER_DX_HOSTNAME=dx.tudominio.com
CLUSTER_PORT=7300
CLUSTER_SYSOP_PORT=8050

# MariaDB - cambialo antes del primer arranque
CLUSTER_DB_USER=sysop
CLUSTER_DB_PASS=change_me
CLUSTER_DB_ROOT_PASSWORD=change_me_root
CLUSTER_DB_NAME=spiderdb

# Usuario telnet interno de Spiderweb (se crea automaticamente)
CLUSTER_SPIDERWEB_USER=SPIDERWEBUSER
CLUSTER_SPIDERWEB_PASSWORD=change_me_web
```

> Nota: `CLUSTER_SPIDERWEB_USER` y `CLUSTER_SPIDERWEB_PASSWORD` se crean automaticamente en DXSpider al arrancar. No hace falta crearlos manualmente.

### 3. Construir y levantar el stack

```bash
docker compose up -d --build
```

En el primer arranque se construyen las imagenes de DXSpider y Spiderweb. Puede tardar unos minutos.

### 4. Comprobar que todo esta funcionando

```bash
docker compose ps
```

Todos los servicios deben aparecer como `Up` o `Up (healthy)`.

### 5. Acceso a las interfaces

| Servicio | URL |
|---|---|
| Spiderweb (spots y estadisticas) | http://localhost/ |
| Consola sysop (ttyd) | http://localhost/console |
| Acceso telnet al cluster | `telnet localhost 7300` |

### 6. Parar y reiniciar

```bash
# Parar
docker compose down

# Iniciar de nuevo (sin reconstruir)
docker compose up -d
```

> Persistencia de datos: los datos se guardan en `./database_data/` (MariaDB) y `./local_data/` (configuracion DXSpider).
