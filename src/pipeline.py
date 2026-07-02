# ==========================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ==========================================
# 2. CARGA Y EXPLORACIÓN DE DATOS
# ==========================================
print("\n--- INICIANDO PIPELINE: CARGA DE DATOS ---")
df = pd.read_csv('../Data/Telco-Customer-Churn.csv')      
print(df.head())

print("\n--- INFORMACIÓN GENERAL ---")
df.info()

print("\n--- ESTADÍSTICAS COMPLETAS ---")
print(df.describe(include='all'))

print(f"\n--- DIMENSIONES DEL DATASET: {df.shape} ---")

# ==========================================
# 3. LIMPIEZA DE DATOS
# ==========================================
print("\n--- ELIMINAR COLUMNA customerID ---")
df = df.drop("customerID", axis=1)

print("\n--- CORREGIR TIPO DE DATO DE TotalCharges ---")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print("\n--- REVISIÓN Y REEMPLAZO DE NULOS EN TotalCharges ---")
df["TotalCharges"] = df["TotalCharges"].fillna(0)
print(f"Nulos restantes:\n{df.isnull().sum()}")

print("\n--- ELIMINAR DUPLICADOS ---")
duplicados = df.duplicated().sum()
print(f"Filas duplicadas encontradas: {duplicados}")
df = df.drop_duplicates()
print(f"Tamaño del dataset tras eliminar duplicados: {df.shape}")

# ==========================================
# 4. VISUALIZACIONES (Comentadas para Docker)
# ==========================================
# En un pipeline automatizado en Docker, no podemos usar plt.show() porque no hay pantalla.
# Si quieres guardar las imágenes en el futuro, usarías plt.savefig('../Data/nombre_grafico.png')

# print("\n--- GENERANDO GRÁFICOS (Guardado en background) ---")
# plt.figure(figsize=(8, 5))
# sns.countplot(data=df, x='Contract', hue='Churn', palette='Set2')
# plt.title('Abandono de Clientes (Churn) según Tipo de Contrato')
# plt.savefig('../Data/contrato_vs_churn.png')
# plt.close()

# plt.figure(figsize=(10, 6))
# sns.histplot(data=df, x='tenure', hue='Churn', multiple='stack', bins=36, palette='Set2')
# plt.title('Distribución de la Antigüedad de Clientes (Tenure) vs Churn')
# plt.savefig('../Data/antiguedad_vs_churn.png')
# plt.close()

# ==========================================
# 5. PREPARACIÓN DE DATOS (PREPROCESSING)
# ==========================================
print("\n--- SEPARACIÓN DE FEATURES (X) Y TARGET (y) ---")
X = df.drop('Churn', axis=1)
y = df['Churn']
print(f"Dimensiones de X: {X.shape} | Dimensiones de y: {y.shape}")

print("\n--- CODIFICACIÓN DE LA VARIABLE OBJETIVO (y) ---")
y = y.map({'No': 0, 'Yes': 1})

print("\n--- ONE-HOT ENCODING PARA LAS FEATURES (X) ---")
X = pd.get_dummies(X, drop_first=True)
X = X.astype(int)
print(f"Nuevas dimensiones de X: {X.shape}")

print("\n--- DIVISIÓN EN CONJUNTOS DE ENTRENAMIENTO Y PRUEBA ---")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"X_train: {X_train.shape} | X_test: {X_test.shape}")

print("\n--- ESCALADO DE DATOS (ESTANDARIZACIÓN) ---")
columnas_continuas = ['tenure', 'MonthlyCharges', 'TotalCharges']
scaler = StandardScaler()

X_train[columnas_continuas] = scaler.fit_transform(X_train[columnas_continuas])
X_test[columnas_continuas] = scaler.transform(X_test[columnas_continuas])

print("\n¡FASE 1 DEL PIPELINE COMPLETADA CON ÉXITO!")
print("Primeros registros de variables continuas escaladas en X_train:")
print(X_train[columnas_continuas].head(3))