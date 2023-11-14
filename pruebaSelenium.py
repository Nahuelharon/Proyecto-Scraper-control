import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_iniciar_ses(self):
        driver = self.driver
        driver.get("https://sigof2.sofse.gob.ar/login")
        time.sleep(2)
        sesion = driver.find_element("xpath","/html/body/div/div[2]/form/div/div/button")
        sesion.click()
        time.sleep(2)
        driver.execute_script("window.open('');")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://sigof2.sofse.gob.ar/planillonVue2/47")
        time.sleep(2)
        #driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


#""" driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")"""
