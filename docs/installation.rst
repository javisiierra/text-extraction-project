Instalación
-----------
Este documento explica cómo instalar y configurar **text-extraction-project** en tu sistema.

Requisitos previos
~~~~~~~~~~~~~~~~~~
- Python 3.8 o superior
- pip
- Docker (opcional, para ejecución en contenedor)

Instalación mediante pip
~~~~~~~~~~~~~~~~~~~~~~~~
```sh
pip install text-extraction-project
```

Instalación mediante entorno virtual
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Instalación con Docker
~~~~~~~~~~~~~~~~~~~~~~~
```sh
docker build -t text-extraction-project .
docker run text-extraction-project
```
