import os
import sys
import asyncio

from logging.config import fileConfig

from sqlalchemy import pool, Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config import settings
from db.base import Base

import models  # noqa: F401


config = context.config

config.set_main_option("sqlalchemy.url", settings.DB_URL)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

DIRECTUS_TABLE_PREFIXES = [
    "directus_",
    "directus_system_",
    "directus_activity_",
    "directus_collections_",
    "directus_fields_",
    "directus_relations_",
    "directus_revisions_",
    "directus_users_",
    "directus_roles_",
    "directus_permissions_",
    "directus_presets_",
    "directus_notifications_",
    "directus_shares_",
    "directus_flows_",
    "directus_operations_",
    "directus_webhooks_",
    "directus_versions_",
    "directus_migrations_",
    "directus_sessions_",
    "directus_settings_",
    "directus_files_",
    "directus_folders_",
    "directus_dashboards_",
    "directus_panels_",
    "directus_translations_",
    "directus_telemetry_",
]


def include_object(object, name, type_, reflected, compare_to):
    if type_ == "table" and name.startswith("directus_"):
        return False
    return True


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = config.attributes.get("connection", None)
    if connectable is None:
        asyncio.run(run_async_migrations())
    else:
        do_run_migrations(connectable)


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
