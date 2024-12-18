import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones.Funciones import Funciones_Globales
from Funciones.Page_Login import Pagina_Login

tg = 5
class base_test(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para el WebDriver de Chrome
        service = Service(executable_path=r"C:\DRIVER\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        # Define el tiempo de espera
        self.t = 4

    def test1(self):
        # Instanciamos la clase Funciones_Globales
        driver = self.driver
        f = Funciones_Globales(driver)
        pg = Pagina_Login(driver)
        pg.Login_Master("https://www.saucedemo.com/v1/","Rodrigo","admin", tg)




    def tearDown(self):
        # Cerrar el navegador después de finalizar las pruebas
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
