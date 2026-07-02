# 1. imagen oficial de Python ligera
FROM python:3.9-slim

# 2. Carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias y las instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo el contenido de tu proyecto al contenedor
COPY Data/ ./Data/
COPY src/ ./src/
CMD ["python", "src/pipeline.py"]