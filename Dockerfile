FROM alpine:3.20

# Argumentos de construcción
# ARG SPIDER_GIT_REPOSITORY=git://scm.dxcluster.org/scm/spider
ARG SPIDER_GIT_REPOSITORY=https://github.com/9M2PJU/dxspider.git
ARG SPIDER_VERSION=mojo
ARG SPIDER_INSTALL_DIR=/spider
ARG SPIDER_USERNAME=sysop
ARG SPIDER_UID=1000

# 1. Instalación de dependencias y compilación
RUN apk update && apk add --no-cache \
    # Herramientas de sistema y runtime
    git \
    nano \
    netcat-openbsd \
    ttyd \
    wget \
    bash \
    mariadb-client \
    mariadb-connector-c \
    # Dependencias de Perl (Binarios de Alpine para mayor velocidad)
    perl \
    perl-db_file \
    perl-digest-sha1 \
    perl-io-socket-ssl \
    perl-net-telnet \
    perl-timedate \
    perl-yaml-libyaml \
    perl-test-simple \
    perl-curses \
    perl-mojolicious \
    perl-math-round \
    perl-json \
    perl-dbd-mysql \
    perl-dbi \
    perl-net-cidr-lite \
    # Paquetes temporales de compilación (se borrarán después)
    && apk add --no-cache --virtual .build-deps \
    build-base \
    perl-dev \
    perl-app-cpanminus \
    ncurses-dev \
    mariadb-dev \
    # Instalación de módulos específicos de CPAN
    && cpanm --no-wget Data::Structure::Util \
    # Configuración de usuario y clonación
    && adduser -D -u ${SPIDER_UID} -h ${SPIDER_INSTALL_DIR} ${SPIDER_USERNAME} \
    && git config --global --add safe.directory ${SPIDER_INSTALL_DIR} \
    && git clone -b ${SPIDER_VERSION} ${SPIDER_GIT_REPOSITORY} ${SPIDER_INSTALL_DIR} \
    # Preparación de directorios
    && mkdir -p ${SPIDER_INSTALL_DIR}/local ${SPIDER_INSTALL_DIR}/local_cmd ${SPIDER_INSTALL_DIR}/local_data \
    # Compilación del cliente C
    && (cd ${SPIDER_INSTALL_DIR}/src && make) \
    # Ajuste de permisos inicial
    && find ${SPIDER_INSTALL_DIR}/. -type d -exec chmod 2775 {} \; \
    && find ${SPIDER_INSTALL_DIR}/. -type f -name '*.pl' -exec chmod 775 {} \; \
    && chown -R ${SPIDER_USERNAME}:${SPIDER_USERNAME} ${SPIDER_INSTALL_DIR} \
    # Limpieza para reducir tamaño de imagen
    && apk del .build-deps \
    && rm -rf /var/cache/apk/* /root/.cpanm

# 2. Configuración de archivos (Solo si no usas volúmenes externos para esto)
# Nota: Si usas volúmenes en docker-compose, estos COPY se sobrescribirán al arrancar.
WORKDIR ${SPIDER_INSTALL_DIR}

# Limpieza de conectores por defecto y copia de los tuyos
RUN rm -rf ${SPIDER_INSTALL_DIR}/connect/*
COPY --chown=${SPIDER_USERNAME}:${SPIDER_USERNAME} ./connect ${SPIDER_INSTALL_DIR}/connect/
COPY --chown=${SPIDER_USERNAME}:${SPIDER_USERNAME} motd ${SPIDER_INSTALL_DIR}/data/
COPY --chown=${SPIDER_USERNAME}:${SPIDER_USERNAME} startup ${SPIDER_INSTALL_DIR}/scripts/
COPY --chown=${SPIDER_USERNAME}:${SPIDER_USERNAME} crontab ${SPIDER_INSTALL_DIR}/local_cmd/

# 3. Script de entrada y permisos finales
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Cambiamos al usuario sysop para seguridad
USER ${SPIDER_USERNAME}

# Exponemos los puertos típicos (ajustables vía ENV en el compose)
EXPOSE 7300 8000

ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]
