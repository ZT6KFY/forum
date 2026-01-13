from logging.config import fileConfig
import os
import sys

from sqlalchemy import create_engine
from alembic import context

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.core.config.settings import settings
from app.core.database.base_model import Base

import app.models  # noqa


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def include_name(name, type_, parent_names):
    if type_ == "schema":
        return name in ["public", "users", "boards", "threads", "posts", "admin_logs"]

    if type_ == "table":
        return True

    return True


def run_migrations_offline():
    url = str(settings.DATABASE_URL).replace("postgresql+asyncpg://", "postgresql://")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_schemas=True,
        include_name=include_name,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(
        str(settings.DATABASE_URL).replace("postgresql+asyncpg://", "postgresql://")
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            include_name=include_name,
            version_table_schema="public",
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
