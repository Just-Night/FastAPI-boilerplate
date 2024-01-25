FROM python:3.9.7

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG APP_USER=appuser

RUN groupadd -r ${APP_USER} -g 1000 && useradd --no-log-init --create-home -u 1000 -r -g ${APP_USER} ${APP_USER}

ARG APP_DIR=/home/${APP_USER}/project/
RUN echo $APP_DIR && mkdir ${APP_DIR} && chown ${APP_USER}:${APP_USER} ${APP_DIR}

COPY ./requirements.txt ${APP_DIR}


RUN set -ex \
    && RUN_DEPS=" \
    libpcre3 \
    mime-support \
    postgresql-client \
    python3-dev \
    musl-dev \
    netcat \
    gdal-bin \
    libgdal-dev \
    gettext \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r ${APP_DIR}requirements.txt


COPY service ${APP_DIR}


COPY ./alembic ${APP_DIR}/alembic
COPY ./alembic.ini ${APP_DIR}
COPY ./local.entrypoint.sh ${APP_DIR}
COPY ./babel.cfg ${APP_DIR}

RUN chmod a+x ${APP_DIR}local.entrypoint.sh && \
    chmod a+x ${APP_DIR}alembic.ini  && \
    chmod a+x ${APP_DIR}alembic  && \
    chmod a+x ${APP_DIR}babel.cfg

#USER ${APP_USER}:${APP_USER}
WORKDIR ${APP_DIR}
EXPOSE 8000
