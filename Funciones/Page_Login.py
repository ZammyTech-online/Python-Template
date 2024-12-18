import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones_Globales

class Pagina_Login():
    def __init__(self, driver):
        self.driver = driver


    def Login_Master(self,url,name,clave, t):
        f = Funciones_Globales(self.driver)
        f.Navegar(url, t)
        f.Texto_Xpath_Valida("//input[contains(@id,'user-name')]", name, t)
        f.Texto_Xpath_Valida("//input[contains(@id,'password')]", clave, t)
        f.Click_Xpath_Valida("//input[contains(@id,'login-button')]", t)
        f.Salida()
