FROM python:3.10

RUN apt-get update && apt-get install -y curl g++ 

# Establecer el directorio de trabajo (aquí es donde estarán tus notebooks)
WORKDIR /home/jovyan/work

# Copiar el archivo de requisitos al contenedor
COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install jupyterlab

# Exponer el puerto 8888 para JupyterLab
EXPOSE 8888

# Comando para arrancar JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

