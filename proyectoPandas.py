import requests
from requests_ntlm import HttpNtlmAuth
#import certifi
from io import StringIO
import pandas as pd

# Desactiva las advertencias de solicitud insegura (puedes omitir esta línea si no quieres ver las advertencias)
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# URL de la página protegida
url = 'https://sigof2.sofse.gob.ar/planillonVue2/38'

#usuario y contraseña de windows
username = "facundo.guerrero"
password = "Inicio16"

#Configuro la ruta del certificado usando certifi
#cert_path = certifi.where()

# Realiza la solicitud de inicio de sesión con autenticación NTLM
response = requests.get(url, auth=HttpNtlmAuth(username,password),verify=False)

# Verifica si la autenticación fue exitosa
if response.status_code == 200:
    # Usa BeautifulSoup para analizar la página y extraer la tabla
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    tabla = soup.find('table')

    # Puedes procesar la tabla según tus necesidades
    # Por ejemplo, puedes usar Pandas para convertir la tabla en un DataFrame
    # import pandas as pd
    #df = pd.read_html(str(tabla))[0]

    # Usa StringIO para envolver la cadena HTML y luego lee la tabla con read_html
    html_str = str(tabla)
    html_io = StringIO(html_str)
    df = pd.read_html(html_io)[0]

    # Ahora puedes trabajar con el DataFrame df que contiene los datos de la tabla

else:
    print("Error de autenticación: ", response.status_code)
