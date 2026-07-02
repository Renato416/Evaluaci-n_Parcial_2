import pandas as pd
from sqlalchemy import create_engine
import logging
import os

# ==========================================
# 1. CONFIGURACIÓN DE LOGS (Registro de errores)
# ==========================================
logging.basicConfig(filename='carga_datos.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Iniciando proceso de carga a PostgreSQL...")

# ==========================================
# 2. CONEXIÓN A LA BASE DE DATOS
# ==========================================
# REEMPLAZA 'TU_CONTRASEÑA_AQUI' POR LA CLAVE QUE CREASTE (ej: postgres o admin)
db_url = 'postgresql://postgres:admin@host.docker.internal:5432/telco_db'
engine = create_engine(db_url)

# ==========================================
# 3. LECTURA DE DATOS VALIDADOS
# ==========================================
# Usamos la ruta directa desde la raíz, igual que en el pipeline
ruta_archivo = 'Data/validated/telco_clean.csv'

if not os.path.exists(ruta_archivo):
    logging.error(f"No se encontró el archivo en {ruta_archivo}")
    print(f"Error: No se encontró el archivo en {ruta_archivo}")
    exit()

try:
    df = pd.read_csv(ruta_archivo)
    logging.info(f"Archivo cargado exitosamente. Total registros: {len(df)}")
    
    # ==========================================
    # 4. CARGA CONTROLADA A POSTGRESQL Y SEPARACIÓN DE RECHAZADOS
    # ==========================================
    print("Iniciando inserción de datos en PostgreSQL...")
    
    # to_sql crea la tabla automáticamente y carga los datos.
    # if_exists='replace' asegura que si lo corres dos veces, se actualice.
    df.to_sql('clientes_telco', engine, if_exists='replace', index=False)
    
    logging.info("Carga de datos exitosa. Todos los registros fueron insertados.")
    print("¡Carga exitosa! Revisa tu base de datos en pgAdmin.")
    
except Exception as e:
    logging.error(f"Error durante la carga de datos: {e}")
    print(f"Ocurrió un error: {e}")