from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.core.config.settings import settings
from app.core.database.base_model import Base

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata


def run_migrations_offline():
    url = str(settings.DATABASE_URL).replace("postgresql+asyncpg://", "postgresql://")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    engine = create_engine(
        str(settings.DATABASE_URL).replace("postgresql+asyncpg://", "postgresql://")
    )
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
