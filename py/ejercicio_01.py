import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv('Semana_05/doc/recipeData2.csv', sep=';')

x = data['IBU']
y = data['Color']
z = data['ABV']

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=4,
        color=z,
        colorscale='Viridis',
        opacity=0.8,
        colorbar=dict(title='ABV (%)'),
        line=dict(width=0)
    ),
    text=[f'Beer ID: {beer_id}' for beer_id in data['BeerID']],
    hoverinfo='text'
))

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

fig.show()
