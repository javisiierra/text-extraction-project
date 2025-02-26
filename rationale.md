Este documento explica cómo se han validado las respuestas obtenidas en el análisis de los artículos. A continuación, se describen los pasos seguidos en el proceso:

# Pasos del Proceso

1) Creación de un pipeline con Grobid y selección inicial de artículos

    Se ha utilizado Grobid para procesar los artículos en formato PDF y extraer información estructurada en XML. La selección de artículos se ha basado en criterios específicos de relevancia.

    El script process_pdf_with_grobid se encarga de enviar cada PDF al servidor de Grobid, recibir el XML procesado y almacenarlo en una carpeta de salida. Posteriormente, estos archivos XML se utilizan para la extracción de información clave.

2) Creación de scripts en Python para responder las preguntas

    Se han desarrollado scripts en Python que analizan los datos extraídos de los artículos y generan respuestas a las preguntas de investigación.

    process_xml analiza los archivos XML obtenidos con Grobid y extrae el título, resumen, palabras clave, número de figuras y enlaces presentes en el documento.

    Se crea un informe individual en PDF para cada artículo, incluyendo la información relevante.

    Se genera una nube de palabras con las palabras clave más repetidas entre todos los artículos.

    Se crea un informe global en PDF con las palabras clave más frecuentes y su conteo.

    Se genera una visualización comparativa del número de figuras en los artículos analizados.