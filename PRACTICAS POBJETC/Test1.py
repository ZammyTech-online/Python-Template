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
        f.Navegar("https://testingqarvn.com.es/prueba-de-campos-checkbox/", tg)

        # Generando los XPaths usando un bucle for
        xpaths = [f"//label[contains(@id,'wsf-1-label-36-row-{i}')]" for i in
                  range(1, 4)]  # Esto genera una lista con los XPaths

        # Usando * para desempaquetar la lista de XPaths y pasarlos como argumentos separados a Check_Xpath_Multiples
        f.Check_Xpath_Multiples(tg, *xpaths)

    def tearDown(self):
        # Cerrar el navegador después de finalizar las pruebas
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
