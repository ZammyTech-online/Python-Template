from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Funciones.Funciones import Funciones_Globales
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Funciones.Funciones import Funciones_Globales
from selenium.webdriver.chrome.service import Service

# Crear una nueva instancia del driver de Chrome
ser = Service("C:\DRIVER\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

# Establecer un tiempo de espera implícito
driver.implicitly_wait(10)

# Crear una nueva instancia de la clase Funciones_Globales con el nombre "f"
f = Funciones_Globales(driver)

# Paso 1: Buscar en Google la palabra "automatización"
f.Navegar("https://www.google.com", 2)

# Esperar hasta que el campo de búsqueda esté disponible
search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

# Buscar el campo de búsqueda y escribir "automatización"
f.Texto_Mixto("name", "q", "automatización", 2)

# Simular la tecla Enter
search_box.submit()

# Paso 2: Buscar el link de la Wikipedia resultante
wikipedia_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'wikipedia.org')]")))
wikipedia_link.click()

# Obtener el enlace de Wikipedia para futuras referencias
enlace_wikipedia = driver.current_url

# Paso 3: Comprobar en qué año se hizo el primer proceso automático
f.Esperar_Elemento("//span[contains(text(), 'año 300 a. C')]", 5)

# Paso 4: Tomar screenshot de la página
#f.Tomar_Screenshot("screenshot_wikipedia.png")

# Cerrar el navegador
driver.quit()