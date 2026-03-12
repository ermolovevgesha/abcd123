FROM python:3.13

RUN apt-get update && apt-get -y install gdal-bin

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync --locked


