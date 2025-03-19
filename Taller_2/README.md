# 🐳 Pipeline de Entrenamiento e Inferencia en ML con Docker

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![JupyterLab](https://img.shields.io/badge/JupyterLab-4.0+-orange.svg)](https://jupyter.org/)
[![Docker](https://img.shields.io/badge/Docker-24.0+-blue.svg)](https://www.docker.com/)
[![uv](https://img.shields.io/badge/uv-package%20installer-purple.svg)](https://github.com/astral-sh/uv)

Este proyecto implementa un entorno containerizado para entrenar modelos de Machine Learning y desplegar una API de inferencia. Se integra uv para la gestión rápida de dependencias y se usan volúmenes compartidos en Docker para que los modelos entrenados en JupyterLab sean accesibles por la API FastAPI.

## 🏗️ Arquitectura

El proyecto consta de dos servicios principales:

- **JupyterLab**: Entorno de desarrollo para entrenamiento de modelos
- **FastAPI**: API REST para realizar inferencias con los modelos entrenados

Los modelos entrenados se comparten entre contenedores mediante un volumen Docker.

```
graph LR
  A[JupyterLab] -->|Entrena y guarda modelos| B[Volumen Compartido]
  B -->|Carga modelos| C[FastAPI]
  D[Cliente] -->|Solicita inferencia| C
```

## ✨ Características

- 🔄 Sincronización automática de modelos entre servicios
- 📦 Gestión de dependencias con `uv` (más rápido y eficiente que pip)
- 🚀 API REST con FastAPI para inferencias
- 📓 JupyterLab para desarrollo y entrenamiento
- 🐳 Completamente containerizado con Docker

## 🚀 Inicio Rápido

1. **Clonar el repositorio**

bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>


2. **Iniciar los servicios**
bash
docker compose up -d


3. **Acceder a los servicios**
- JupyterLab: http://localhost:8080
- FastAPI: http://localhost:8081
- Documentación API: http://localhost:8081/docs

## 📁 Estructura del Proyecto

```
Taller_2
├── docker-compose.yaml
├── data/
│   ├── penguins_lter.csv
│   └── penguins_size.csv
├── jupyterlab/
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── uv.lock
│   └── train.py
└── fastapi/
    ├── Dockerfile
    ├── pyproject.toml
    ├── uv.lock
    └── main.py
```



## 🔧 Configuración

El proyecto utiliza Docker Compose para orquestar los servicios:

- **JupyterLab**:
  - Puerto: 8080
  - Volúmenes: 
    - `models_volume`: Para modelos entrenados
    - `./data`: Para datos de entrenamiento

- **FastAPI**:
  - Puerto: 8081
  - Volumen: `models_volume` (compartido con JupyterLab)

## 💻 Uso

1. **Entrenamiento de Modelos**
   - Accede a JupyterLab en `http://localhost:8080`
   - Los modelos se guardan automáticamente en el volumen compartido

2. **Inferencias**
   - Utiliza la API REST en `http://localhost:8081`
   - Consulta la documentación en `http://localhost:8081/docs`

## 🛠️ Tecnologías

- [Docker](https://www.docker.com/)
- [JupyterLab](https://jupyter.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [uv](https://github.com/astral-sh/uv)
- [Python 3.10](https://www.python.org/)

