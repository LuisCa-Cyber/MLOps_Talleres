FROM python:3.10-slim

# Instala curl para instalar uv
RUN apt-get update && apt-get install -y curl

# Instala uv y actualiza el PATH
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /home/app

# Copia los archivos de dependencias
COPY pyproject.toml .
COPY uv.lock .

# Sincroniza las dependencias
RUN uv sync

# Copia el resto de archivos (por ejemplo, train.py)
COPY . .

# Expone el puerto de JupyterLab
EXPOSE 8888

CMD ["uv", "run", "jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
