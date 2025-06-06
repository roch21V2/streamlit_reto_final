FROM python:3.10-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app

COPY . .

RUN uv sync --no-cache-dir

CMD ["uv", "run", "streamlit", "run", "src/app.py"]



