# Telco Customer Churn Prediction

## Descripción del Proyecto
Este proyecto tiene como objetivo desarrollar un modelo predictivo capaz de identificar clientes con alta probabilidad de abandonar una compañía de telecomunicaciones (churn).

La predicción temprana permitirá implementar estrategias de retención y mejorar la satisfacción del cliente.

---

## Objetivo
Construir un modelo de Machine Learning para predecir el churn de clientes utilizando variables demográficas, servicios contratados e historial de consumo.

---

## Dataset

### Variables Demográficas
- `gender`: Male / Female
- `SeniorCitizen`: 0 = menor de 65 años, 1 = mayor de 65 años
- `Partner`: Yes / No
- `Dependents`: Yes / No

### Servicios Contratados
- `Contract`: Month-to-month, 1 year, 2 years
- `PhoneService`: Yes / No
- `MultipleLines`: Yes / No / No phone service
- `InternetService`: DSL, Fiber optic, No

Servicios adicionales:
- `OnlineSecurity`
- `OnlineBackup`
- `DeviceProtection`
- `TechSupport`
- `StreamingTV`
- `StreamingMovies`

### Historial de Consumo
- `MonthlyCharges`
- `TotalCharges`
- `tenure`
- `PaymentMethod`
- `PaperlessBilling`

### Variable Objetivo
- `Churn`: Yes / No

---

## Tecnologías Utilizadas
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

## Flujo del Proyecto
1. Limpieza y preparación de datos
2. Análisis exploratorio (EDA)
3. Ingeniería de variables
4. Entrenamiento de modelos
5. Evaluación de métricas
6. Interpretación de resultados

---

## Modelos Evaluados
- Logistic Regression
- Random Forest
- XGBoost

---

## Métricas
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
