import pandas as pd
import plotly.graph_objects as go

# Leer el archivo CSV
data = pd.read_csv('Semana_05/doc/recipeData2.csv', sep=';')  # Asegúrate de usar el separador correcto

# Extraer las columnas para las coordenadas
x = data['IBU']  # Amargor
y = data['Color']  # Color
z = data['ABV']  # Porcentaje de alcohol

# Crear un gráfico 3D con Plotly
fig = go.Figure()

# Agregar las cervezas como puntos en el gráfico
fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=4,
        color=z,  # Color basado en el ABV
        colorscale='Viridis',  # Mapa de colores
        opacity=0.8,
        colorbar=dict(title='ABV (%)'),
        line=dict(width=0)
    ),
    text=[f'Beer ID: {beer_id}' for beer_id in data['BeerID']],  # Etiquetas de cervezas
    hoverinfo='text'  # Mostrar etiquetas al pasar el mouse
))

# Personalizar el gráfico
fig.update_layout(
    title='Gráfico 3D de Cervezas',
    scene=dict(
        xaxis_title='IBU',
        yaxis_title='Color',
        zaxis_title='ABV (%)',
        xaxis=dict(showbackground=False, showgrid=False),
        yaxis=dict(showbackground=False, showgrid=False),
        zaxis=dict(showbackground=False, showgrid=False),
    ),
    margin=dict(l=0, r=0, b=0, t=50),
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white')
)

# Mostrar el gráfico
fig.show()
