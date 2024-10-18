# Generador de Imágenes desde HTML

Esta aplicación Flask permite convertir contenido HTML en una imagen PNG y almacenarla en un bucket público de Amazon S3. La aplicación expone un endpoint `/generate` que acepta una solicitud POST con el HTML y devuelve la URL de la imagen generada.

## Requisitos Previos

- Python 3.8+
- Cuenta de AWS con acceso a S3
- Bucket S3 configurado para acceso público

## Instalación

1. Clonar el repositorio:
   ```
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Crear un entorno virtual e instalar las dependencias:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Instalar Playwright y sus dependencias:
   ```
   playwright install
   ```

4. Configurar las variables de entorno:
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```
   AWS_ACCESS_KEY_ID=tu_access_key
   AWS_SECRET_ACCESS_KEY=tu_secret_key
   S3_BUCKET_NAME=nombre_de_tu_bucket
   S3_REGION=region_de_tu_bucket
   ```

## Uso

1. Iniciar la aplicación:
   ```
   python app.py
   ```

2. Realizar una solicitud POST al endpoint `/generate`:
   ```
   curl -X POST -H "Content-Type: application/json" -d '{"html": "<html><body><h1>Hola Mundo</h1></body></html>", "width": 600, "height": 400}' http://localhost:5000/generate
   ```

3. La respuesta incluirá la URL de la imagen generada en S3.

## Desarrollo

- `app.py`: Contiene la lógica principal de la aplicación Flask.
- `main.py`: Script independiente para generar imágenes localmente.

## Despliegue

Para desplegar en producción, considera usar un servidor WSGI como Gunicorn y configurar un proxy inverso con Nginx.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de crear un pull request.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
