from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Funciones.Funciones import Funciones_Globales

# Crear una nueva instancia del driver de Chrome
ser = Service("C:\\DRIVER\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="C:\\DRIVER\\chromedriver.exe", options=op)

# Crear una nueva instancia de la clase Funciones_Globales con el nombre "f"
f = Funciones_Globales(driver)

# Paso 1: Buscar en Google la palabra "automatización"
f.Navegar("https://www.google.com", 2)

# Esperar hasta que el campo de búsqueda esté disponible
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'APjFqb')))

# Buscar el campo de búsqueda y escribir "automatización"
f.Texto_Mixto("id", "APjFqb", "automatización", 2)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'APjFqb'))).submit()

# Paso 2: Buscar el link de Wikipedia resultante
wikipedia_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'wikipedia.org')]")))
wikipedia_link.click()

# Obtener el enlace de Wikipedia para futuras referencias
enlace_wikipedia = driver.current_url

# Paso 3: Comprobar en qué año se hizo el primer proceso automático
# Usar tu función para esperar hasta que el elemento esté presente
elemento = f.Esperar_Elemento_xpath('//*[@id="mw-content-text"]/div[1]/p[28]', 10)

# Obtener el texto del elemento
texto_elemento = elemento.text

# Buscar '300 a. C.' en el texto del elemento
indice_inicio = texto_elemento.find('300 a. C.')

if indice_inicio != -1:
    # Si se encontró '300 a. C.', extraerlo
    texto_extraido = texto_elemento[indice_inicio:indice_inicio + len('300 a. C.')]
    print(texto_extraido)
else:
    print("'300 a. C.' no se encontró en el texto del elemento")

# Llamar a la función scroll_y_captura
f.scroll_y_captura2('//*[@id="mw-content-text"]/div[1]/p[28]')

# Cerrar el navegador
driver.quit()
