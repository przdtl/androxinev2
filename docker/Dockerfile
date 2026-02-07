FROM python:3.11 AS builder

ARG INSTALL_DEV=false

WORKDIR /app

ENV POETRY_VERSION=1.8.4 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

COPY pyproject.toml poetry.lock ./

RUN if [ "$INSTALL_DEV" = "true" ]; then \
        poetry install --with dev; \
    else \
        poetry install --without dev --no-root; \
    fi

FROM python:3.11-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin

COPY alembic.ini ./
COPY ./src ./src
COPY ./docker/scripts ./scripts

ENTRYPOINT ["sh", "./scripts/entrypoint.sh"]

