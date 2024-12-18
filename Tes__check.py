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

driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
driver.maximize_window()# Espera hasta que el campo de mensaje de usuario esté presente
#driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

t=2
btn1 =wait.until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@type,'checkbox')])[1]")))
time.sleep(t)



time.sleep(t)
driver.close()