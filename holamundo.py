

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service("C:\DRIVER\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


driver.get("https://www.smartketingjapan.online")
print(driver.title)

driver.close()