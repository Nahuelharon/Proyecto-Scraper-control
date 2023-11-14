from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from io import StringIO

# Configura el navegador (asegúrate de tener geckodriver o chromedriver en tu PATH)
driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

# URL de la página protegida
url = 'https://sigof2.sofse.gob.ar/planillonVue2/38'

#usuario y contraseña de windows
username = "facundo.guerrero"
password = "Inicio16"

try:

    # Abre la página en el navegador
    driver.get(url)

    # Ingresa las credenciales si es necesario (puedes personalizar esto según la página)
    #driver.find_element_by_name('username').send_keys(username)
    #driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('submit').click()

    # Espera a que la página se cargue completamente (puedes ajustar el tiempo según sea necesario)
    driver.implicitly_wait(10)

    # Extrae el HTML de la página
    html_str = driver.page_source

    # Cierra el navegador
    driver.quit()

    # Usa StringIO para envolver la cadena HTML y luego lee la tabla con read_html
    html_io = StringIO(html_str)
    df = pd.read_html(html_io)[0]

    # Ahora puedes trabajar con el DataFrame df que contiene los datos de la tabla
except Exception as e:
    print(f"Error: {e}")

#finally:
    # Cierra el navegador
    #driver.quit()
