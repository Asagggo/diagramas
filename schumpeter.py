from graphviz import Digraph
from IPython.display import display, Image

# Define el diagrama
dot = Digraph()

# Configuración global
dot.attr(size='10,10')  # Ajusta el tamaño de la imagen
dot.attr(dpi='300')  # Configura la calidad de la imagen
dot.attr(rankdir='TB')  # Orientación del gráfico de arriba a abajo (vertical)
dot.attr(bgcolor='white')  # Color de fondo del gráfico

# Estilo de los nodos
node_attrs = {
    'style': 'filled',
    'shape': 'box',
    'fillcolor': 'lightyellow',
    'color': 'black',
    'fontname': 'Arial',
    'fontsize': '10',
    'fontcolor': 'black'
}

# Estilo de los subgráficos
subgraph_attrs = {
    'color': 'lightyellow',
    'labeljust': 'c',
    'labelloc': 't',
    'style': 'filled',
    'fontname': 'Arial',
    'fontsize': '12',
    'fontcolor': 'black'
}

# Estilo de las flechas
edge_attrs = {
    'color': 'black',
    'fontname': 'Arial',
    'fontsize': '10',
    'fontcolor': 'black'
}

# Subgráficos para cada etapa
with dot.subgraph(name='cluster_0') as c:
    c.attr(**subgraph_attrs, label='Introducción de Nuevas Innovaciones')
    c.node('A1', 'Nuevos Productos', **node_attrs)
    c.node('A2', 'Nuevos Métodos de Producción', **node_attrs)
    c.node('A3', 'Apertura de Nuevos Mercados', **node_attrs)
    c.node('A4', 'Conquista de Nuevas Fuentes de Suministros', **node_attrs)
    c.node('A5', 'Reorganización de Industrias Existentes', **node_attrs)

with dot.subgraph(name='cluster_1') as c:
    c.attr(**subgraph_attrs, label='Desplazamiento y Obsolescencia')
    c.node('B1', 'Obsolescencia de Tecnologías y Métodos Anteriores', **node_attrs)
    c.node('B2', 'Eliminación de Métodos Obsoletos', **node_attrs)

with dot.subgraph(name='cluster_2') as c:
    c.attr(**subgraph_attrs, label='Impacto en el Mercado Laboral')
    c.node('C1', 'Desempleo a Corto Plazo', **node_attrs)
    c.node('C2', 'Desaparición de Empleos Tradicionales', **node_attrs)
    c.node('C3', 'Adaptación a Nuevas Demandas del Mercado', **node_attrs)

with dot.subgraph(name='cluster_3') as c:
    c.attr(**subgraph_attrs, label='Reacción de las Empresas y la Sociedad')
    c.node('D1', 'Resistencia a Innovaciones Importantes', **node_attrs)
    c.node('D2', 'Impacto en Estructuras Existentes', **node_attrs)
    c.node('D3', 'Importancia de Permitir la Entrada de lo Nuevo', **node_attrs)

with dot.subgraph(name='cluster_4') as c:
    c.attr(**subgraph_attrs, label='Ciclos Económicos y Adaptación')
    c.node('E1', 'Ciclos de Prosperidad y Depresión', **node_attrs)
    c.node('E2', 'Influencia de la Innovación Empresarial', **node_attrs)
    c.node('E3', 'Adaptación del Sistema', **node_attrs)

# Conexiones entre las etapas
dot.edge('A1', 'B1', **edge_attrs)
dot.edge('B1', 'C1', **edge_attrs)
dot.edge('C1', 'D1', **edge_attrs)
dot.edge('D1', 'E1', **edge_attrs)
dot.edge('E3', 'A5', **edge_attrs)

# Guardar y renderizar el diagrama
dot.render('diagrama_1_schumpeter', format='png', cleanup=True)