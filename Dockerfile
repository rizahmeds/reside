FROM python:3.13-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /code

# Copy dependency files
COPY pyproject.toml uv.lock /code/

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy application code
COPY . /code/