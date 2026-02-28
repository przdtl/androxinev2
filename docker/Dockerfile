FROM python:3.12-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ARG GROUP

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    bash -c '\
        if [ -n "$GROUP" ]; then \
            echo "Installing dependencies for group: $GROUP"; \
            uv sync --group "$GROUP" --locked --no-editable; \
        else \
            echo "Installing default dependencies"; \
            uv sync --locked --no-editable; \
        fi \
    '


FROM python:3.12-slim

WORKDIR /app

ENV PYTHONPATH=src \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY --from=builder --chown=app:app /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH"

COPY alembic.ini ./
COPY ./src ./src
COPY ./docker/scripts ./scripts

RUN chmod +x ./scripts

ENTRYPOINT ["sh", "./scripts/entrypoint.sh"]
