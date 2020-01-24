
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
	Descomentar para visualizar al mismo tiempo que se procesa la prueba
	print('Información general de la prueba \n'
		  + 'Para su correcto funcionamiento debe esta decide corriendo en local o en un servidor por parte de un proveedor de servicios web. \n')
		  + 'El fin de la prueba es verificar que el id de la votación es un numero mayor que 0'
	'''
	votingID = input('Qué votación se esta examinando : ')

	driver = webdriver.Chrome('/Users/antonio/Desktop/chromedriver')
	driver.get("http://localhost:8000/visualizer/" + votingID)
	element = driver.find_element_by_id("votingID")


	numbers = re.findall(r'\d+', element.text)

	#print(numbers)

	verification = float(numbers[0]) > 0
	print('Prueba superada ? : ' + str(verification))


''' Descomentar para probar las pruebas que aparecen acontinuación
voting_id_is_positive()
'''





