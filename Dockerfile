# 1. Usar una imagen oficial de Python ligera
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias y las instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo el código y datos al contenedor
COPY . .

# 5. Comando por defecto: Ejecutar limpieza y luego carga a BD
CMD ["sh", "-c", "python src/pipeline.py && python src/load_data.py"]