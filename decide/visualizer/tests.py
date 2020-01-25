
# Create your tests here.
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import requests
import unittest
import re
import math



def voting_id_is_positive():
	'''
	Descomentar para visualizar al mismo tiempo que se procesa la prueba'''
	print('Información general de la prueba \n'
		  + 'Para su correcto funcionamiento debe esta decide corriendo en local o en un servidor por parte de un proveedor de servicios web. \n'
		  + 'El fin de la prueba es verificar que el id de la votación es un numero mayor que 0')
	
	votingID = input('Qué votación se esta examinando : ')

	driver = webdriver.Chrome('./chromedriver_ubuntu')
	driver.get("http://localhost:8000/visualizer/" + votingID)
	element = driver.find_element_by_id("votingID")


	numbers = re.findall(r'\d+', element.text)

	#print(numbers)

	verification = float(numbers[0]) > 0
	print('Criterio para el id superado : ' + str(verification))

def test_enviar_email_correcto():

        driver = webdriver.Chrome('./chromedriver_ubuntu')

        driver.get("http://127.0.0.1:8000/visualizer/1/")

        driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[2]').send_keys("decide123456789@gmail.com")

        driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[3]').click()
        
        verification = str(driver.find_element_by_xpath('/html/body/div/section/div[2]/ul/li/div').text).startswith('El email ha sido enviado!')

        print('Criterio para test_enviar_email_correcto : ' + str(verification)) 

        driver.close()

        driver.quit()

def test_enviar_email_mal():

        driver = webdriver.Chrome('./chromedriver_ubuntu')

        driver.get("http://127.0.0.1:8000/visualizer/1/")

        driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[2]').send_keys("emailmal.com")

        driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[3]').click()
        
        verification = driver.find_elements_by_xpath('/html/body/div/section/div[2]/ul/li/div').count('El email ha sido enviado!') is 0

        driver.close()

        driver.quit()

        

        print('Criterio para test_enviar_email_mal : ' + str(verification)) 

''' Descomentar para probar las pruebas que aparecen acontinuación'''

#voting_id_is_positive()
test_enviar_email_correcto()
test_enviar_email_mal()






