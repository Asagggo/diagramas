mermaid_code = """
graph TD
    subgraph Introducción_de_Nuevas_Innovaciones
        A1[Nuevos Productos]
        A2[Nuevos Métodos de Producción]
        A3[Apertura de Nuevos Mercados]
        A4[Conquista de Nuevas Fuentes de Suministros]
        A5[Reorganización de Industrias Existentes]
    end
    subgraph Desplazamiento_y_Obsolescencia
        B1[Obsolescencia de Tecnologías y Métodos Anteriores]
        B2[Eliminación de Métodos Obsoletos]
    end
    subgraph Impacto_en_el_Mercado_Laboral
        C1[Desempleo a Corto Plazo]
        C2[Desaparición de Empleos Tradicionales]
        C3[Adaptación a Nuevas Demandas del Mercado]
    end
    subgraph Reacción_de_las_Empresas_y_la_Sociedad
        D1[Resistencia a Innovaciones Importantes]
        D2[Impacto en Estructuras Existentes]
        D3[Importancia de Permitir la Entrada de lo Nuevo]
    end
    subgraph Ciclos_Económicos_y_Adaptación
        E1[Ciclos de Prosperidad y Depresión]
        E2[Influencia de la Innovación Empresarial]
        E3[Adaptación del Sistema]
    end

    Introducción_de_Nuevas_Innovaciones --> Desplazamiento_y_Obsolescencia
    Desplazamiento_y_Obsolescencia --> Impacto_en_el_Mercado_Laboral
    Impacto_en_el_Mercado_Laboral --> Reacción_de_las_Empresas_y_la_Sociedad
    Reacción_de_las_Empresas_y_la_Sociedad --> Ciclos_Económicos_y_Adaptación
    Ciclos_Económicos_y_Adaptación --> Introducción_de_Nuevas_Innovaciones
"""

import matplotlib.pyplot as plt
from mermaid import render_diagram

result = render_diagram({'mermaidCode': mermaid_code})
diagram_url = result['diagram']['diagramUrl']

# Display the diagram
from IPython.display import Image, display
display(Image(url=diagram_url))