ARG build_for=linux/amd64

FROM --platform=$build_for python:3.10-slim-bullseye AS python_node

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV PIP_NO_CACHE_DIR 1

WORKDIR /usr/app

ENV PATH="/opt/node-v12.22.12-linux-x64/bin:${PATH}"
RUN apt-get update && apt-get install -y curl unzip
RUN curl https://nodejs.org/dist/v12.22.12/node-v12.22.12-linux-x64.tar.gz |tar xzf - -C /opt/

FROM python_node as poetry


ENV POETRY_VERSION 1.3.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN pip install "poetry==${POETRY_VERSION}"

COPY . ./
RUN poetry install --no-interaction --no-ansi --no-root -vvv


FROM python_node as runtime
ENV PATH="/usr/app/.venv/bin:$PATH"
ENV HOME="/usr/app"
COPY --from=poetry /usr/app /usr/app
RUN pc init
ENTRYPOINT ["pc", "run", "--env", "prod"]
