import asyncio
from playwright.async_api import async_playwright
from PIL import Image
import io

async def html_to_png(html_content, width, height):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': width, 'height': height})
        
        # {{ Eliminar la interceptación de solicitudes WOFF2 }}
        # await page.route("**/*.woff2", lambda route: route.abort())
        
        # {{ Eliminar las definiciones manuales de @font-face }}
        # font_css = """
        # @font-face {
        #     font-family: 'Inter';
        #     src: url('https://fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1ZL7.woff2') format('woff2');
        #     font-weight: 400;
        #     font-style: normal;
        # }
        # @font-face {
        #     font-family: 'Inter';
        #     src: url('https://fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1ZL7.woff2') format('woff2');
        #     font-weight: 700;
        #     font-style: normal;
        # }
        # @font-face {
        #     font-family: 'Inter';
        #     src: url('https://fonts.gstatic.com/s/inter/v12/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1ZL7.woff2') format('woff2');
        #     font-weight: 800;
        #     font-style: normal;
        # }
        # """
        # html_content = html_content.replace('</head>', f'<style>{font_css}</style></head>')
        
        await page.set_content(html_content)
        
        # {{ Añadir espera para cargar todas las fuentes }}
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

async def main():
    # HTML de entrada (reemplaza esto con tu variable de entrada HTML)
    input_html = """
<html><head>
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1, width=600px, height=237px">
    
    
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,800;1,700&amp;display=swap">
    
    <style>
        body {
            margin: 0;
            line-height: normal;
            font-family: 'Inter', sans-serif;
        }
    </style>
    
    
</head>
<body>
    
    <div style="width: 600px;  position: relative;  height: 237px;  text-align: left;  font-size: 12px;  color: #fff;  font-family: Inter;">
        <div style="position: absolute;  top: 0px;  left: 0px;  border-radius: 20px;  background: linear-gradient(90deg, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2)), #F15252;  width: 632px;  height: 237px;  overflow: hidden;">
            <div style="position: absolute;  top: 0px;  left: 347px;  width: 268px;  height: 237px;">
                <div style="position: absolute;  top: 85px;  left: 190px;  border-radius: 16px;  background: linear-gradient(180deg, rgba(255, 255, 255, 0.17), rgba(255, 255, 255, 0.25));  width: 78px;  height: 203px;">
                </div>
                <div style="position: absolute;  top: -66px;  left: 96px;  border-radius: 16px;  background: linear-gradient(180deg, rgba(255, 255, 255, 0.17), rgba(255, 255, 255, 0.25));  width: 142px;  height: 369px;">
                </div>
                <div style="position: absolute;  top: 24px;  left: 0px;  border-radius: 16px;  background: linear-gradient(180deg, rgba(255, 255, 255, 0.17), rgba(255, 255, 255, 0.25));  width: 142px;  height: 369px;">
                </div>
            </div>
            <div style="position: absolute;  top: 39px;  left: 33px;  border-radius: 6px;  background-color: rgba(255, 255, 255, 0.25);  height: 23px;  display: flex;  flex-direction: row;  align-items: center;  justify-content: center;  padding: 10px;  box-sizing: border-box;">
                <i style="position: relative;  font-weight: 700;">CURSO</i>
            </div>
            <div style="position: absolute;  top: 0px;  left: 536px;  border-radius: 0px 0px 16px 16px;  background: linear-gradient(180deg, rgba(255, 255, 255, 0.8), #fff);  width: 78px;  height: 81px;  display: flex;  flex-direction: row;  align-items: flex-end;  justify-content: center;  padding: 20px 10px;  box-sizing: border-box;">
                <img style="width: 40px;  position: relative;  height: 45px; filter: brightness(0);" alt="" src="https://cdn.openwebinars.net/media/academy/course/iso-logo.svg">
                
            </div>
            <img style="position: absolute;  top: 0px;  left: 370px;  width: 239px;  height: 237px;  object-fit: cover;  object-position: top;filter: grayscale(100%);" alt="" src="https://cdn.openwebinars.net/media/teachers/David_sanchez_frontal.png">
            
                    <div style="position: absolute; top: 70px; left: 33px; font-size: 40px; line-height: 41px; font-weight: 800; display: flex; width: 337px; height: 120px; justify-content: flex-start; align-items: center; text-align: center;">  
                        <div style="width: 100%; text-align: left;">
                            Implementación de la ISO 27001 
                        </div>
                    </div>
            <div style="position: absolute;  top: 194px;  left: 33px;  display: flex;  flex-direction: row;  align-items: center;  justify-content: flex-end;  gap: 7px;  font-size: 10px;">
                <div style="position: relative;">Con nuestro experto:</div>
                <div style="border-radius: 6px;  background-color: rgba(255, 255, 255, 0.35);  height: 23px;  display: flex;  flex-direction: row;  align-items: center;  justify-content: center;  padding: 10px;  box-sizing: border-box;">
                    <i style="position: relative;  font-weight: 700;">David</i><i style="position: relative;  font-weight: 700; margin-left:4px">Sánchez Alonso</i>
                </div>
            </div>
        </div>
    </div>
    
    
    
    

</body></html>
    """

    # Tamaño del viewport
    viewport_width = 650
    viewport_height = 237

    # Nombre del archivo de salida
    output_file = 'output.png'

    try:
        image = await html_to_png(input_html, viewport_width, viewport_height)
        image.save(output_file, 'PNG')
        print(f"La imagen se ha guardado como {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
