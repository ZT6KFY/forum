FROM python:3.13-slim AS builder
ENV POETRY_VERSION=1.8.4 POETRY_HOME="/opt/poetry" POETRY_NO_INTERACTION=1 POETRY_VIRTUALENVS_IN_PROJECT=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ENV PATH="$POETRY_HOME/bin:$PATH"
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc libpq-dev && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==${POETRY_VERSION}"

COPY pyproject.toml poetry.lock ./
RUN poetry check && poetry install --without dev --no-root -vvv

COPY . /app

FROM python:3.13-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends libpq5 && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app /app
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["python3", "main.py"]
