# text-extraction-project

# Análisis de Artículos Científicos con GROBID

Este proyecto analiza artículos en formato PDF extrayendo información relevante como resúmenes, palabras clave, figuras mencionadas y enlaces. Genera informes en PDF y visualizaciones como nubes de palabras y comparaciones de figuras.

# Características

Procesamiento de PDFs con GROBID.

Extracción de metadatos, palabras clave y referencias.

Generación de informes automáticos en PDF.

Creación de una nube de palabras basada en los resúmenes.

Comparación del número de figuras mencionadas por artículo.

# Requisitos

Python 3.8+

GROBID corriendo en http://localhost:8070

# Dependencias de Python:

pip install -r requirements.txt

# Instalación y Uso

        Opción 1: Entorno Virtual

        python -m venv venv
        source venv/bin/activate  # En Windows: venv\Scripts\activate
        pip install -r requirements.txt
        python programa.py <carpeta_con_pdfs>

        Opción 2: Docker

        docker build -t analisis-pdf .
        docker run -v $(pwd)/pdfs:/app/pdfs analisis-pdf pdfs

# Estructura de Salida

procesados/ → Carpeta con los archivos procesados.

wordcloud_global.png → Nube de palabras clave.

resumen_palabras.pdf → Informe de palabras clave.

comparacion_figuras.png → Comparación del número de figuras por artículo.

# Documentación

La documentación completa está disponible en ReadTheDocs.

# Licencia

Este proyecto está bajo la licencia MIT. Ver LICENSE para más detalles.

