import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Cargar datos
df = pd.read_csv('Semana_05/doc/recipeData2.csv', sep=';')

# Limpiar y convertir columnas necesarias
cols = ['Efficiency', 'IBU', 'ABV', 'BoilTime', 'PrimaryTemp', 'UserId', 'Size(L)', 'StyleID']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['BrewMethod'] = df['BrewMethod'].fillna('Desconocido')

# Eliminar filas con datos clave faltantes
df_clean = df.dropna(subset=['Efficiency', 'IBU', 'ABV', 'BoilTime', 'PrimaryTemp'])

# Limitar eficiencia a rango 0–100
df_clean = df_clean[(df_clean['Efficiency'] >= 0) & (df_clean['Efficiency'] <= 100)]

# Crear figura
fig = go.Figure()

# Agrupar por método de elaboración (All Grain, Extract, BIAB, etc.)
for method in df_clean['BrewMethod'].unique():
    group = df_clean[df_clean['BrewMethod'] == method]
    
    fig.add_trace(go.Scatter3d(
        x=group['IBU'],
        y=group['ABV'],
        z=group['PrimaryTemp'],
        mode='markers',
        marker=dict(
            size=np.clip(group['BoilTime'] / 10, 4, 20),
            color=group['Efficiency'],
            colorscale='Plasma',
            colorbar=dict(title='Eficiencia (%)'),
            opacity=0.8
        ),
        name=f'Método: {method}',
        text=[
            f"<b>Usuario:</b> {uid}<br>"
            f"<b>Estilo:</b> {style}<br>"
            f"<b>Tamaño:</b> {size} L<br>"
            f"<b>BoilTime:</b> {bt} min<br>"
            f"<b>Eficiencia:</b> {eff}%"
            for uid, style, size, bt, eff in zip(
                group['UserId'],
                group['StyleID'],
                group['Size(L)'],
                group['BoilTime'],
                group['Efficiency']
            )
        ],
        hoverinfo='text'
    ))

# Personalización del gráfico
fig.update_layout(
    title='🌾 Análisis 3D de Recetas de Cerveza por Método y Eficiencia',
    scene=dict(
        xaxis=dict(title='IBU (Amargor)', backgroundcolor="black", gridcolor="gray"),
        yaxis=dict(title='ABV (%)', backgroundcolor="black", gridcolor="gray"),
        zaxis=dict(title='Temp. Fermentación (°C)', backgroundcolor="black", gridcolor="gray")
    ),
    legend=dict(x=0, y=1, font=dict(color='white')),
    margin=dict(l=10, r=10, b=10, t=60),
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white')
)

fig.show()
