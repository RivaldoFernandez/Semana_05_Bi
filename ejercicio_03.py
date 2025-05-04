import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

df = pd.read_csv('Semana_05/doc/housing-with-missing-1.csv', sep=';')
df.replace(["NA", "null", "none", ""], np.nan, inplace=True)
df = df.apply(pd.to_numeric, errors='coerce')

print("Antes de imputar:\n", df.isnull().sum())

imp = IterativeImputer(random_state=0)
df_imp = pd.DataFrame(imp.fit_transform(df), columns=df.columns)

print("\nDespués de imputar:\n", df_imp.isnull().sum())

plt.figure(figsize=(12, 5))
for i, data in enumerate([df, df_imp]):
    plt.subplot(1, 2, i+1)
    sns.heatmap(data.isnull(), cbar=True, cmap="YlGnBu", yticklabels=False)
    plt.title("Antes" if i == 0 else "Después")
    plt.xlabel("Variables")
    plt.ylabel("Filas")

plt.suptitle("Valores Faltantes - Antes y Después de Imputación", fontsize=14)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
