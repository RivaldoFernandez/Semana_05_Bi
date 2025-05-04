import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Semana_05/doc/housing-with-missing-1.csv', sep=';')

print("Valores faltantes antes de la imputación:")
print(df.isnull().sum())

plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Valores Faltantes en el DataFrame (Antes de Imputación)')
plt.show()

df.fillna(df.mean(), inplace=True)

print("\nValores faltantes después de la imputación:")
print(df.isnull().sum())

plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Valores Faltantes en el DataFrame (Después de Imputación)')
plt.show()

