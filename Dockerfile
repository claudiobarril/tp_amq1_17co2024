# Usar una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar herramientas de compilación
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN pip install poetry

# Copiar el archivo pyproject.toml y poetry.lock
COPY pyproject.toml poetry.lock ./

# Instalar las dependencias del proyecto
RUN poetry config virtualenvs.create false && poetry install

# Copiar el resto de los archivos del proyecto
COPY . .

# Exponer el puerto que usará Jupyter Notebook
EXPOSE 8888

# Comando para ejecutar Jupyter Notebook
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8895", "--no-browser", "--allow-root"]
