import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

ser = Service("C:\DRIVER\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.maximize_window()# Espera hasta que el campo de mensaje de usuario esté presente
#driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

t=.5

btn = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-message']")))


btn.send_keys("Bienvenidos a selenium" + Keys.TAB + Keys.ENTER)
time.sleep(t)


# Espera hasta que el campo 'value1' esté presente
value1 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'value1')]")))
value1.send_keys("5" + Keys.TAB + "5" + Keys.ENTER)

# Espera hasta que el botón para obtener el total esté clickeable
total_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='gettotal']//button")))
total_button.click()

# Puedes agregar más esperas explícitas según sea necesario para otros elementos en la página.

# Espera un poco antes de cerrar para asegurarte de que todos los comandos se hayan ejecutado
time.sleep(t)
time.sleep(2)

driver.close()