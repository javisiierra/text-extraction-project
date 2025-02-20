# Objetivo

El objetivo del código es automatizar el proceso de extracción, análisis y generación de informes a partir de documentos académicos en formato PDF. Utiliza GROBID para convertir los archivos PDF en XML (TEI), extrae información clave como resúmenes, palabras clave y menciones de figuras, y genera un informe en formato PDF con visualizaciones.

# Componentes Principales

1. Procesamiento de PDF con GROBID

    Se envía el archivo PDF al servicio de GROBID mediante una petición HTTP.

    GROBID devuelve un archivo XML con la estructura del documento.

    El XML resultante se guarda en una carpeta específica para cada documento.

2. Procesamiento del XML

    Se extraen el resumen y las palabras clave utilizando xml.etree.ElementTree.

    Se analizan las menciones a figuras en el cuerpo del texto.

    Se extraen enlaces de referencia.

3. Generación de Nube de Palabras

    Se genera una nube de palabras a partir del resumen y palabras clave utilizando WordCloud.

    La imagen se guarda en la carpeta del documento.

4. Generación del Informe en PDF

    Se usa FPDF para crear un informe con:

    Resumen y palabras clave.

    Conteo de figuras mencionadas en el artículo.

    Lista de enlaces encontrados.

    Imagen de la nube de palabras.

    Cada informe se guarda en una carpeta exclusiva para el artículo.

5. Visualización del Total de Figuras

    Se genera un gráfico de barras con el número total de figuras por artículo usando matplotlib.

    El gráfico se guarda en la carpeta procesados como estudioFiguras.png.

# Beneficios del Enfoque

Automatización Completa: Procesa varios archivos PDF sin intervención manual.

Organización Estructurada: Cada artículo tiene su propia carpeta con los resultados.

Análisis Visual: La nube de palabras y el gráfico de figuras facilitan la interpretación de los datos.

Escalabilidad: Puede adaptarse fácilmente a grandes volúmenes de documentos.

Este código proporciona un flujo de trabajo eficiente para la extracción de información académica, con posibilidades de extensión y mejora.

