# text-extraction-project
# Análisis de Artículos Científicos con GROBID

Este proyecto analiza artículos en formato PDF extrayendo información relevante como resúmenes, palabras clave, figuras mencionadas y enlaces. Genera informes en PDF y visualizaciones como nubes de palabras y comparaciones de figuras.

## Características
- Procesamiento de PDFs con GROBID.
- Extracción de metadatos, palabras clave y referencias.
- Generación de informes automáticos en PDF.
- Creación de una nube de palabras basada en los resúmenes.
- Comparación del número de figuras mencionadas por artículo.
- **Tests automáticos con `pytest` para validar el correcto funcionamiento.**

## Requisitos
- Python 3.8+
- GROBID corriendo en `http://localhost:8070`
- Dependencias de Python:
  ```sh
  pip install -r requirements.txt
  ```

## Instalación y Uso
### Opción 1: Entorno Virtual
```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python programa.py <carpeta_con_pdfs>
```

### Opción 2: Docker
```sh
# Construir la imagen
docker build -t analisis-pdf .

# Ejecutar el contenedor con volumen para PDFs
docker run -v $(pwd)/pdfs:/app/articles analisis-pdf
```

## Ejecución de Tests
Para validar el correcto funcionamiento, ejecuta los tests con `pytest`:
```sh
pytest test_programa.py
```
Si no tienes `pytest`, instálalo con:
```sh
pip install pytest
```
Si usas un entorno virtual, actívalo antes de correr los tests:
```sh
source venv/bin/activate  # En Windows: venv\Scripts\activate
pytest test_programa.py
```

## Estructura de Salida
- `procesados/` → Carpeta con los archivos procesados.
- `wordcloud_global.png` → Nube de palabras clave.
- `resumen_palabras.pdf` → Informe de palabras clave.
- `comparacion_figuras.png` → Comparación del número de figuras por artículo.

## Documentación
La documentación completa está disponible en [ReadTheDocs](https://readthedocs.org/).

### Generación de Documentación Local
Para generar la documentación localmente, instala `sphinx` y ejecuta:
```sh
pip install sphinx
cd docs
make html
```
Los archivos generados estarán en `docs/_build/html/`.

## Notas Importantes
- **No subas el entorno virtual (`venv/`) a GitHub**. Asegúrate de incluirlo en tu `.gitignore`.
- Grobid se ejecutará dentro del contenedor, por lo que no es necesario instalarlo manualmente.

## Cita y Referencia  

Si utilizas este proyecto en tu investigación, por favor cita el trabajo usando Zenodo:  

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14961847.svg)](https://doi.org/10.5281/zenodo.14961847)

Puedes encontrar más detalles en la página de Zenodo del proyecto.

## Licencia
Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.



