import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
data = pd.read_csv('Semana_05/doc/housing-with-missing-1.csv', sep=';')

# Mostrar los datos originales
print("Datos originales:")
print(data)

# Imputar valores faltantes con la media de cada columna
data_imputed_mean = data.fillna(data.mean())

# Visualizar los datos originales y los imputados
plt.figure(figsize=(12, 6))

# Gráfico de los datos originales
plt.subplot(1, 2, 1)
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title('Datos Originales con Valores Faltantes')

# Gráfico de los datos imputados
plt.subplot(1, 2, 2)
sns.heatmap(data_imputed_mean.isnull(), cbar=False, cmap='viridis')
plt.title('Datos Imputados (Media)')

plt.show()
