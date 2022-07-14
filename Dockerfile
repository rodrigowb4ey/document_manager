# syntax=docker/dockerfile:1
FROM python:3.9.12-alpine3.15

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.1.14

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./poetry.lock /app/
COPY ./pyproject.toml /app/
COPY ./entrypoint.sh /app/

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /app/

ENTRYPOINT ["/app/entrypoint.sh"]