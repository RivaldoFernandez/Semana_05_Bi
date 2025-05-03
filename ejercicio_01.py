import numpy as np
import plotly.graph_objects as go

# Parámetros de la galaxia elíptica
num_stars = 5000
a = 10  # Semi-eje mayor
b = 6   # Semi-eje menor
z_height = 3  # Altura máxima en el eje Z

# Generar coordenadas en un elipsoide
theta = np.random.rand(num_stars) * 2 * np.pi
r = np.random.rand(num_stars) * np.sqrt(np.random.rand(num_stars))  # Distribución radial

# Coordenadas en el espacio elíptico
x = a * r * np.cos(theta)
y = b * r * np.sin(theta)
z = np.random.uniform(-z_height, z_height, num_stars)  # Altura aleatoria para el eje Z

# Crear un gráfico 3D con Plotly
fig = go.Figure()

# Agregar las estrellas como puntos en el gráfico
fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=4,
        color=np.sqrt(x**2 + y**2),  # Color basado en la distancia radial
        colorscale='Viridis',  # Mapa de colores
        opacity=0.8,
        colorbar=dict(title='Brillo Estelar'),
        line=dict(width=0)
    ),
    text=[f'Star {i}' for i in range(num_stars)],  # Etiquetas de estrellas
    hoverinfo='text'  # Mostrar etiquetas al pasar el mouse
))

# Personalizar el gráfico
fig.update_layout(
    title='Galaxia Elíptica Simulada en 3D',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
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
