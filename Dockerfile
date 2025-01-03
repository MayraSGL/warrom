FROM python:3.9-slim

# Agregar información del build
LABEL maintainer="Developer"
LABEL version="1.0"
LABEL description="Contenedor para ejecutar holaMundo.py con verbose logging"

# Configurar variables de entorno para Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY holaMundo.py .

# Asegurar permisos de escritura con más verbosidad
RUN echo "Configurando permisos del directorio..." && \
    chmod 755 /app && \
    echo "Permisos del directorio configurados: $(ls -la /app)" && \
    chmod 644 holaMundo.py && \
    echo "Permisos del archivo configurados: $(ls -la holaMundo.py)"

# Verificar la instalación de Python
RUN python --version && \
    python -c "import sys; print(f'Python path: {sys.path}')"

CMD ["python", "holaMundo.py"] 