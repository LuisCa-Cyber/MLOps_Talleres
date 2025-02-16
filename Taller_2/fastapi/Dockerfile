FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl

# Instala uv y actualiza el PATH
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /home/app

COPY pyproject.toml .
COPY uv.lock .
RUN uv sync

COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
