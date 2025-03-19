--------------------------------------------------
# 🐳 Pipeline de MLflow y MinIO: Entrenamiento e Inferencia de Modelos en ML con Docker

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)  
[![JupyterLab](https://img.shields.io/badge/JupyterLab-4.0+-orange.svg)](https://jupyter.org/)  
[![Docker](https://img.shields.io/badge/Docker-24.0+-blue.svg)](https://www.docker.com/)  
[![uv](https://img.shields.io/badge/uv-package%20installer-purple.svg)](https://github.com/astral-sh/uv)

# Nota importante: 
Este proyecto se encuentra desplegado en la MV 10.43.101.173


Este proyecto implementa un entorno containerizado para entrenar modelos de Machine Learning y desplegar una API de inferencia. Se utiliza FastAPI para exponer un servicio REST que carga y sirve modelos registrados en MLflow. Además, se dispone de un entorno de JupyterLab para el entrenamiento y experimentación, y se emplea MinIO como sistema de almacenamiento de artefactos.

--------------------------------------------------
## 🏗️ Arquitectura

El proyecto consta de los siguientes servicios:

- JupyterLab: Entorno de desarrollo para entrenamiento de modelos, registro en MLflow y guardado de artefactos en MinIO.
- FastAPI: API REST para realizar inferencias usando los modelos registrados en MLflow.
- MLflow: Gestión del ciclo de vida de los modelos (registro, versionado y promoción a Production).
- MinIO: Almacenamiento de artefactos (modelos, archivos, etc.).
- MySQL: Base de datos para almacenar los metadatos de MLflow (o también puede usarse SQLite en algunos casos).

Los servicios se comunican mediante volúmenes y puertos expuestos para simular un entorno de producción.


## ✨ Características

- Entrenamiento y registro de modelos con MLflow.
- Almacenamiento de artefactos en MinIO (simulando un bucket S3).
- API de inferencia desarrollada en FastAPI.
- Entorno interactivo de JupyterLab para experimentación y entrenamiento.
- Orquestación de servicios mediante Docker Compose.

--------------------------------------------------
## 🚀 Inicio Rápido

1. Clonar el repositorio:
git clone https://github.com/LuisCa-Cyber/MLOps_Talleres.git cd MLOps_Talleres/Taller_MLFlow


2. Iniciar los servicios:
docker compose up -d


3. Acceder a los servicios:
- JupyterLab: http://localhost:8080
- FastAPI: http://localhost:8081
- Documentación de la API: http://localhost:8081/docs
- MinIO: http://localhost:9001 (Usuario: admin, Contraseña: supersecret)

--------------------------------------------------
## 📁 Estructura del Proyecto
```
Taller_MLFlow/
├── notebooks/
│   ├── penguins_lter.csv     # Datos de entrenamiento
│   └── penguins_size.csv     # Datos de entrenamiento
│   └── Notebook Entrenamiento.py              # Script de entrenamiento y registro en MLflow
├── jupyterlab/
│   ├── Dockerfile            # Dockerfile para el entorno JupyterLab
│   ├── requirements.txt      # Dependencias para entrenamiento y experimentación
└── fastapi/
 ├── Dockerfile            # Dockerfile para la API FastAPI
 ├── requirements.txt      # Dependencias para inferencia (FastAPI)
 └── app.py                # Código principal de la API
├── docker-compose.yml        # Orquestación de servicios (MySQL, MinIO, FastAPI, JupyterLab)
├── mlflow_serv.service       # Archivo systemd para iniciar MLflow Server

```
--------------------------------------------------
## 🔧 Configuración

El proyecto utiliza Docker Compose para gestionar los servicios:

- JupyterLab:
- Puerto: 8080
- Monta volúmenes para compartir datos y modelos.

- FastAPI:
- Puerto: 8081
- Carga modelos desde MLflow utilizando MinIO como artifact store.
- Variables de entorno configuradas:
 - MLFLOW_S3_ENDPOINT_URL: http://10.43.101.173:9000
 - AWS_ACCESS_KEY_ID: admin
 - AWS_SECRET_ACCESS_KEY: supersecret

- MinIO:
- Puertos: 9000 (API) y 9001 (consola web)

- MLflow y MySQL:
- MLflow utiliza MySQL (o SQLite en algunos casos) para almacenar metadatos y MinIO para los artefactos.

--------------------------------------------------
## 💻 Uso

### Entrenamiento y Registro de Modelos

1. Accede a JupyterLab en http://localhost:8080.
2. Ejecuta el script de entrenamiento (train.py) para entrenar los modelos y registrarlos en MLflow.
- Los modelos se registran con nombres: random_forest, decision_tree, svm y logistic_regression.
- MLflow subirá los artefactos (modelos) a MinIO.

### Promoción y Carga de Modelos en la API

1. Desde la API (FastAPI), se ejecuta automáticamente una función que promociona versiones específicas de los modelos a Production.
2. Luego, se cargan los modelos desde MLflow en la API para que estén listos para servir inferencias.
3. Si necesitas recargar o promocionar nuevamente, la API cuenta con los siguientes endpoints:
- POST /promote_models/ : Promociona versiones a Production.
- POST /reload_models/ : Recarga los modelos desde MLflow.
- PUT /select_model/{model_name} : Cambia el modelo seleccionado.
- POST /predict/ : Realiza una inferencia.

--------------------------------------------------
## 🛠️ Requisitos

### JupyterLab (entrenamiento)
Archivo: requirements_jupyterlab.txt
pandas numpy matplotlib seaborn scikit-learn mlflow sqlalchemy pymysql uvicorn jupyterlab boto3

### FastAPI (inferencia)
Archivo: requirements_fastapi.txt
mlflow pymysql scikit-learn==1.6.1 pandas fastapi uvicorn numpy==2.2.4 joblib dill boto3 psutil==7.0.0

--------------------------------------------------
## 🚀 Pruebas de la API

1. Accede a la documentación interactiva en:
   http://localhost:8081/docs

2. Realiza una predicción enviando un JSON con las características de un pingüino:
   {
     "culmen_length_mm": 50.0,
     "culmen_depth_mm": 15.0,
     "flipper_length_mm": 200.0,
     "body_mass_g": 4000.0,
     "island": 1
   }

3. Cambia el modelo de inferencia (si es necesario) usando:
   - PUT /select_model/{model_name} (donde {model_name} es: random_forest, decision_tree, svm o logistic_regression).

