import pandas as pd
import plotly.graph_objects as go

# Leer el archivo CSV
data = pd.read_csv('Semana_05/doc/recipeData2.csv', sep=';')

# Convertir columnas necesarias a numéricas
cols = ['IBU', 'Color', 'ABV', 'BoilTime', 'Efficiency', 'PrimaryTemp']
for col in cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Limpiar datos
data_clean = data.dropna(subset=cols)

# Coordenadas
x = data_clean['IBU']           # Amargor
y = data_clean['Color']         # Color
z = data_clean['ABV']           # Alcohol
size = data_clean['BoilTime']   # Tamaño del punto
color = data_clean['Efficiency']  # Eficiencia para colores

# Texto para hover detallado
hover_text = [
    f"<b>Beer ID:</b> {row.BeerID}<br>"
    f"<b>Estilo:</b> {row.StyleID}<br>"
    f"<b>IBU:</b> {row.IBU}<br>"
    f"<b>Color:</b> {row.Color}<br>"
    f"<b>ABV:</b> {row.ABV}%<br>"
    f"<b>BoilTime:</b> {row.BoilTime} min<br>"
    f"<b>Efficiency:</b> {row.Efficiency}%<br>"
    f"<b>Temp. Fermentación:</b> {row.PrimaryTemp} °C"
    for _, row in data_clean.iterrows()
]

# Crear figura
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=size / 10,  # Escalar tamaño
        sizemode='diameter',
        color=color,
        colorscale='Turbo',  # Colores vivos para eficiencia
        colorbar=dict(title='Efficiency (%)'),
        opacity=0.9,
        line=dict(width=0)
    ),
    text=hover_text,
    hoverinfo='text'
))

# Leyenda extendida
leyenda = (
    "<b>LEYENDA:</b><br>"
    "<b>Eje X:</b> IBU – Amargor<br>"
    "<b>Eje Y:</b> Color – SRM<br>"
    "<b>Eje Z:</b> ABV – Alcohol %<br>"
    "<b>Tamaño:</b> Tiempo de ebullición (BoilTime)<br>"
    "<b>Color:</b> Eficiencia del proceso (Efficiency %)<br>"
    "<b>Hover:</b> Info técnica detallada"
)

# Agregar anotación tipo leyenda
fig.add_annotation(
    showarrow=False,
    text=leyenda,
    xref="paper", yref="paper",
    x=0, y=1.08,
    align="left",
    bgcolor="rgba(20,20,20,0.7)",
    font=dict(color="white", size=12)
)

# Personalización estética
fig.update_layout(
    title='🍻 Cervezas en 3D: Amargor, Color, Alcohol, Eficiencia y Más',
    scene=dict(
        xaxis_title='IBU (Amargor)',
        yaxis_title='Color (SRM)',
        zaxis_title='ABV (%)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        zaxis=dict(showgrid=False),
    ),
    margin=dict(l=10, r=10, b=10, t=90),
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white')
)

# Mostrar
fig.show()
