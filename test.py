import requests
import json

# URL de la API
url = "https://imagetool.openwebinars.email/generate"

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

# Datos para enviar en el cuerpo de la petición
datos = {
    "html": input_html,
    "width": 800,
    "height": 237
}

# Cabeceras de la petición
cabeceras = {
    "Content-Type": "application/json"
}

# Realizar la petición POST
respuesta = requests.post(url, data=json.dumps(datos), headers=cabeceras)

# Verificar el estado de la respuesta
if respuesta.status_code == 200:
    print("Petición exitosa")
    print("Respuesta:", respuesta.json())
else:
    print("Error en la petición")
    print("Código de estado:", respuesta.status_code)
    print("Respuesta:", respuesta.text)