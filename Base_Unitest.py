import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException


class base_test(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=r"C:\DRIVER\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        # driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
        t = 4

    def test1(self):
        driver = self.driver
        driver.get("https://testingqarvn.com.es/combobox/")
        driver.maximize_window()
        time.sleep(4)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()






