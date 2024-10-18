import os
import asyncio
import uuid
from flask import Flask, request, jsonify
from playwright.async_api import async_playwright
from PIL import Image
import io
import boto3
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de AWS S3
S3_BUCKET = os.getenv('S3_BUCKET_NAME')
S3_REGION = os.getenv('S3_REGION')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# Inicializar el cliente de S3
s3_client = boto3.client(
    's3',
    region_name=S3_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

async def html_to_png(html_content, width, height):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': width, 'height': height})
        
        await page.set_content(html_content)
        
        # Esperar a que todas las fuentes se carguen
        await page.wait_for_load_state('networkidle')
        await page.evaluate("""
        () => {
            return document.fonts.ready;
        }
        """)
        
        screenshot = await page.screenshot(full_page=True, type='png')
        
        await browser.close()
        
        # Convertir el screenshot a una imagen PIL
        image = Image.open(io.BytesIO(screenshot))
        
        # Recortar la imagen al tamaño del viewport
        image = image.crop((0, 0, width, height))
        
        return image

def upload_to_s3(image, filename):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    s3_client.upload_fileobj(
        img_byte_arr,
        S3_BUCKET,
        filename,
        ExtraArgs={'ContentType': 'image/png', 'ACL': 'public-read'}
    )
    
    s3_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{filename}"
    return s3_url

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    html_content = data.get('html', '')
    
    if not html_content:
        return jsonify({'error': 'No se proporcionó contenido HTML.'}), 400
    
    viewport_width = data.get('width', 600)
    viewport_height = data.get('height', 237)
    
    output_filename = f"{uuid.uuid4()}.png"
    
    try:
        image = asyncio.run(html_to_png(html_content, viewport_width, viewport_height))
        image_url = upload_to_s3(image, output_filename)
        
        return jsonify({'image_url': image_url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
