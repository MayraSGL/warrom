import sys
import os
from datetime import datetime

def main():
    try:
        print(f"[{datetime.now()}] Iniciando el programa...")
        print(f"[{datetime.now()}] Python version: {sys.version}")
        print(f"[{datetime.now()}] Directorio actual: {os.getcwd()}")
        
        mensaje = "¡Hola Mundo desde Python a Docker!"
        print(f"[{datetime.now()}] Mensaje preparado: {mensaje}")
        
        print(f"[{datetime.now()}] Intentando imprimir mensaje...")
        print(mensaje)
        
        print(f"[{datetime.now()}] Intentando escribir en archivo...")
        print(f"[{datetime.now()}] Verificando permisos de escritura...")
        
        ruta_archivo = 'output.txt'
        print(f"[{datetime.now()}] Ruta del archivo: {os.path.abspath(ruta_archivo)}")
        
        if os.path.isdir(ruta_archivo):
            raise ValueError(f"{ruta_archivo} es un directorio, no un archivo.")
        # Escribir el mensaje en un archivo
        with open(ruta_archivo, 'w') as f:
            f.write(mensaje)
            print(f"[{datetime.now()}] Contenido escrito en el archivo")
        
        # Verificar que el archivo se creó correctamente
        if os.path.exists(ruta_archivo):
            print(f"[{datetime.now()}] Verificación: Archivo creado exitosamente")
            print(f"[{datetime.now()}] Tamaño del archivo: {os.path.getsize(ruta_archivo)} bytes")
            
        print(f"[{datetime.now()}] Proceso completado exitosamente")
            
    except Exception as e:
        print(f"[{datetime.now()}] ERROR CRÍTICO: {str(e)}")
        print(f"[{datetime.now()}] Tipo de error: {type(e).__name__}")
        print(f"[{datetime.now()}] Detalles del sistema:")
        print(f"[{datetime.now()}] - OS: {os.name}")
        print(f"[{datetime.now()}] - Permisos del directorio: {oct(os.stat('.').st_mode)[-3:]}")
        sys.exit(1)

if __name__ == "__main__":
    main()