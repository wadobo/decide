from django.test import TestCase

import unittest
from selenium import webdriver
# Create your tests here.



class TestEmailBien(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Firefox()



    def test_enviar_email_correcto(self):

        

        self.driver.get("http://127.0.0.1:8000/visualizer/1/")

        self.driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[2]').send_keys("decide123456789@gmail.com")

        self.driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[3]').click()
        
        self.assertTrue(self.driver.find_element_by_xpath('/html/body/div/section/div[2]/ul/li/div'))

        self.driver.close() 



    def test_enviar_email_mal(self):
        
        
        self.driver.get("http://127.0.0.1:8000/visualizer/1/")

        self.driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[2]').send_keys("emailmal.com")

        self.driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[3]').click()
        
        self.assertFalse(self.driver.find_elements_by_xpath('/html/body/div/section/div[2]/ul/li/div'))   

        self.driver.close() 

        

    def tearDown(self):
        self.driver.quit




if __name__ == '__main__':
    unittest.main()   