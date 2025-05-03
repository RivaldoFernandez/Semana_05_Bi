import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Habilitar el IterativeImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Cargar el dataset
data = pd.read_csv('Semana_05/doc/housing-with-missing-1.csv', sep=';')

# Mostrar los datos originales
print("Datos originales:")
print(data)

# Crear el imputador Multivariate
imputer_mvi = IterativeImputer()

# Imputar los valores faltantes
data_imputed_mvi = imputer_mvi.fit_transform(data)

# Convertir de nuevo a DataFrame
data_imputed_mvi = pd.DataFrame(data_imputed_mvi, columns=data.columns)

# Visualizar los datos originales y los imputados
plt.figure(figsize=(12, 6))

# Gráfico de los datos originales
plt.subplot(1, 2, 1)
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title('Datos Originales con Valores Faltantes')

# Gráfico de los datos imputados
plt.subplot(1, 2, 2)
sns.heatmap(data_imputed_mvi.isnull(), cbar=False, cmap='viridis')
plt.title('Datos Imputados (Multivariate)')

plt.show()
