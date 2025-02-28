Referencia de API
-----------------
Esta sección describe los métodos y clases disponibles en **text-extraction-project**.

```python
from text_extraction import Analyzer

analyzer = Analyzer("example.pdf")
result = analyzer.extract_metadata()
print(result)
```

Principales métodos
~~~~~~~~~~~~~~~~~~~~
- `extract_metadata()`: Obtiene metadatos del documento.
- `generate_wordcloud()`: Genera y guarda una nube de palabras clave.
- `count_figures()`: Cuenta la cantidad de figuras en el artículo.
- `extract_links()`: Extrae los enlaces presentes en el documento.
