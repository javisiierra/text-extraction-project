# Imagen base con Java y Python
FROM openjdk:11-jre-slim

# Configurar el directorio de trabajo
WORKDIR /app

# Instalar Python y herramientas necesarias
RUN apt-get update && apt-get install -y \
    python3 python3-pip wget unzip curl \
    && rm -rf /var/lib/apt/lists/*

# Descargar y configurar Grobid
RUN wget https://github.com/kermitt2/grobid/archive/refs/heads/master.zip -O /tmp/grobid.zip \
    && unzip /tmp/grobid.zip -d /tmp/ \
    && mv /tmp/grobid-master /grobid \
    && rm /tmp/grobid.zip

# Compilar Grobid
WORKDIR /grobid
RUN chmod +x gradlew && ./gradlew clean build

# Volver a la app y copiar los archivos del proyecto
WORKDIR /app
COPY . /app

# Instalar dependencias de Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Exponer puertos para Grobid
EXPOSE 8070

# Iniciar Grobid y el script principal asegurando que Grobid está corriendo
CMD exec sh -c "cd /grobid && ./gradlew run & while ! curl -s http://localhost:8070/api/isalive > /dev/null; do sleep 5; done && python3 programa.py articles"
