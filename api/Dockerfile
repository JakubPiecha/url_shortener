FROM python:3.11 AS development

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV POETRY_VERSION=1.5.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME='/usr/local'

COPY ./install-poetry.py ./
RUN python3 install-poetry.py ./ --version 1.5.1 \
    && $POETRY_HOME/bin/poetry --version

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi --no-root

RUN apt-get update && apt-get install -y netcat

COPY ./entrypoint.sh ./

ENTRYPOINT ["./entrypoint.sh"]

COPY . .

FROM development as prod

COPY --from=development /app /app

RUN poetry install --without dev --sync



