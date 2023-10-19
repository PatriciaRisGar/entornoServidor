# Imagen Python
FROM python:3.10.12

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY ventana.py controlador.py requirements.txt README.txt /app/

# Instala las dependencias si es necesario
RUN pip install -r requirements.txt

# Comando para ejecutar cuando el contenedor se inicia
CMD ["python", "ventana.py"]
