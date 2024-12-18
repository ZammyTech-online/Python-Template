import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones.Funciones import Funciones_Globales
from Funciones.Page_Login import Pagina_Login


class base_test(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para el WebDriver de Chrome
        service = Service(executable_path=r"C:\DRIVER\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        # Define el tiempo de espera
        self.t = 4

    def test1(self):
        # Instanciamos la clase Funciones_Globales
        f = Funciones_Globales(self.driver)

        # Navegar al sitio
        f.Navegar("https://www.saucedemo.com/v1/", 0.1)

        # Ingresamos el nombre de usuario y contraseña usando ID
        f.Texto_ID_Valida("user-name", "Juan", self.t)
        f.Texto_ID_Valida("password", "admin", self.t)

        # Hacemos clic en el botón de inicio de sesión usando ID
        f.Click_ID_Valida("login-button", self.t)

    def tearDown(self):
        # Cerrar el navegador después de finalizar las pruebas
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
