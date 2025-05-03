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

# Asignar un grupo basado en la proximidad
coords = np.array(list(zip(x, y, z)))

# Umbral de proximidad para agrupar las estrellas
threshold = 2  # Distancia máxima para considerar que dos estrellas están en el mismo grupo

# Inicializamos un array para los grupos
groups = np.full(num_stars, -1)

# Función para agrupar por proximidad (distancia euclidiana)
group_id = 0
for i in range(num_stars):
    if groups[i] == -1:  # Si la estrella aún no está asignada a ningún grupo
        # Encuentra las estrellas dentro del umbral de proximidad
        distances = np.sqrt((coords[:, 0] - coords[i, 0])**2 + (coords[:, 1] - coords[i, 1])**2 + (coords[:, 2] - coords[i, 2])**2)
        group_members = np.where(distances < threshold)[0]
        
        # Asignamos a todas las estrellas cercanas al mismo grupo
        groups[group_members] = group_id
        group_id += 1

# Convertimos a un DataFrame
df = {'x': x, 'y': y, 'z': z, 'grupo': groups}

# -------------------- Visualización de la Galaxia y Grupos ---------------------
fig_3d = go.Figure()

# Agregar las estrellas a los grupos en el gráfico 3D
for group in np.unique(df['grupo']):
    group_data = {'x': [], 'y': [], 'z': []}
    for i in range(num_stars):
        if df['grupo'][i] == group:
            group_data['x'].append(df['x'][i])
            group_data['y'].append(df['y'][i])
            group_data['z'].append(df['z'][i])

    fig_3d.add_trace(go.Scatter3d(
        x=group_data['x'], 
        y=group_data['y'], 
        z=group_data['z'],
        mode='markers',
        name=f'Grupo {group}' if group != -1 else 'Ruido',  # Etiqueta el grupo como "Ruido" si es ruido
        marker=dict(
            size=4,
            color=group,  # Color según el grupo
            colorscale='Viridis',  # Mapa de colores
            opacity=0.8,
            colorbar=dict(title='Grupos Estelares')
        ),
        text=[f'Star {i}' for i in range(len(group_data))],  # Etiquetas de estrellas
        hoverinfo='text'  # Mostrar etiquetas al pasar el mouse
    ))

# Personalizar el gráfico 3D
fig_3d.update_layout(
    title='Galaxia con Agrupación Estelar por Proximidad en 3D',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    margin=dict(l=0, r=0, b=0, t=50),
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white')
)

# Mostrar el gráfico 3D
fig_3d.show()




