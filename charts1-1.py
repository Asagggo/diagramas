import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de Asistentes Virtuales y Chatbots
asistentes_virtuales = [
    {"Servicio": "Siri (Apple)", "Objetivo": "Realizar tareas mediante comandos de voz como enviar mensajes, hacer llamadas, establecer recordatorios y buscar información.", "Fecha de Lanzamiento": "2010"},
    {"Servicio": "Google Assistant (Google)", "Objetivo": "Asistente personal que realiza tareas cotidianas como enviar mensajes, hacer llamadas, controlar dispositivos inteligentes y proporcionar información.", "Fecha de Lanzamiento": "2016"},
    {"Servicio": "Alexa (Amazon)", "Objetivo": "Controlar dispositivos inteligentes, reproducir música, proporcionar información del clima y noticias, y realizar compras en Amazon.", "Fecha de Lanzamiento": "2014"},
    {"Servicio": "Cortana (Microsoft)", "Objetivo": "Ayudar a gestionar tareas como establecer recordatorios, enviar correos electrónicos y buscar información en internet. Actualmente se enfoca más en aplicaciones empresariales.", "Fecha de Lanzamiento": "2014"},
    {"Servicio": "Mitsuku (Pandorabots)", "Objetivo": "Mantener conversaciones naturales con los usuarios, ganadora de múltiples premios Loebner.", "Fecha de Lanzamiento": "2005"},
    {"Servicio": "Google Gemini (Google)", "Objetivo": "Integrarse con servicios de Google como Maps y Calendar, gestionar tareas, reproducir música y proporcionar respuestas mediante un modelo de lenguaje multimodal avanzado.", "Fecha de Lanzamiento": "2023 (anteriormente conocido como Google Bard)"},
]

# Datos de Servicios de Inteligencia Artificial para Productividad Empresarial
servicios_productividad = [
    {"Servicio": "IBM Watson", "Objetivo": "Watson ofrece soluciones de inteligencia artificial para empresas, incluyendo análisis de datos, procesamiento de lenguaje natural, y herramientas de automatización. Se utiliza en diversas industrias para mejorar la eficiencia y la toma de decisiones.", "Fecha de Lanzamiento": "2006"},
    {"Servicio": "Microsoft Azure AI", "Objetivo": "Azure AI proporciona servicios de inteligencia artificial y aprendizaje automático que permiten a las empresas desarrollar aplicaciones inteligentes, automatizar procesos y analizar grandes volúmenes de datos.", "Fecha de Lanzamiento": "2010"},
    {"Servicio": "Amazon Web Services (AWS) AI", "Objetivo": "AWS AI ofrece una variedad de servicios de inteligencia artificial que incluyen reconocimiento de imágenes, procesamiento de lenguaje natural, y análisis de datos, diseñados para ayudar a las empresas a innovar y optimizar sus operaciones.", "Fecha de Lanzamiento": "2006"},
    {"Servicio": "Google Cloud AI", "Objetivo": "Google Cloud AI proporciona herramientas de inteligencia artificial y aprendizaje automático para empresas, permitiendo la creación de aplicaciones inteligentes y la automatización de procesos empresariales.", "Fecha de Lanzamiento": "2017"},
    {"Servicio": "Salesforce Einstein", "Objetivo": "Salesforce Einstein ofrece capacidades de inteligencia artificial integradas en la plataforma Salesforce, ayudando a las empresas a obtener insights a partir de sus datos de clientes y a automatizar tareas de ventas, servicio al cliente y marketing.", "Fecha de Lanzamiento": "2016"},
]

# Crear DataFrames
df_asistentes_virtuales = pd.DataFrame(asistentes_virtuales)
df_servicios_productividad = pd.DataFrame(servicios_productividad)

# Configuración de estilo para las tablas
sns.set(style="whitegrid")

def plot_dataframe(df, title, filename):
    fig, ax = plt.subplots(figsize=(12, 4))  # Ajusta el tamaño según tus necesidades
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(1.2, 1.2)
    plt.title(title)
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()

# Exportar DataFrames a imágenes
plot_dataframe(df_asistentes_virtuales, "Asistentes Virtuales y Chatbots", "asistentes_virtuales.png")
plot_dataframe(df_servicios_productividad, "Servicios de Inteligencia Artificial para Productividad Empresarial", "servicios_productividad.png")

# Mostrar los DataFrames
print("Asistentes Virtuales y Chatbots:")
print(df_asistentes_virtuales)
print("\nServicios de Inteligencia Artificial para Productividad Empresarial:")
print(df_servicios_productividad)