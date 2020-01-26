
# Create your tests here.
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import requests
import unittest
import re
import math
import os
import time



def voting_id_is_positive():
	'''
	Descomentar para visualizar al mismo tiempo que se procesa la prueba
	print('Información general de la prueba \n'
		  + 'Para su correcto funcionamiento debe esta decide corriendo en local o en un servidor por parte de un proveedor de servicios web. \n')
		  + 'El fin de la prueba es verificar que el id de la votación es un numero mayor que 0'
	'''
	votingID = input('Qué votación se esta examinando : ')

	driver = webdriver.Chrome('./chromedriver')
	driver.get("http://localhost:8000/visualizer/" + votingID)
	element = driver.find_element_by_id("votingID")


	numbers = re.findall(r'\d+', element.text)

	#print(numbers)

	verification = float(numbers[0]) > 0
	print('Criterio para el id superado : ' + str(verification))


''' Descomentar para probar las pruebas que aparecen acontinuación

voting_id_is_positive()

'''

def pruebaPDFCSV():
	
	#Opciones para la descarga
	options = Options()
	options.add_experimental_option("prefs", {
  	"download.default_directory": r"/home/rog0d/Escritorio",
 	 "download.prompt_for_download": False,
  	"download.directory_upgrade": True,
  	"safebrowsing.enabled": True
	})

	driver = Chrome(executable_path="./chromedriver_ubuntu", 
	options=options)


	Vid = input('ID de la votación a probar: ')
	driver.get("http://localhost:8000/visualizer/"+Vid)
	
	#busqueda y click de los botones
	btnPdf = driver.find_element_by_id('pdf').click()
	btnCsv = driver.find_element_by_id('csv').click()
	
	#Contador para las descargas
	time_to_wait = 10
	time_counter = 0
	while not os.path.exists("/home/rog0d/Escritorio"):
		time.sleep(1)
		time_counter += 1
		if time_counter > time_to_wait:break
	print("descargas realizadas")



def prueba_enviar_email_correcto():

        driver = webdriver.Chrome(executable_path="./chromedriver_ubuntu")

        driver.get("http://127.0.0.1:8000/visualizer/1/")

        driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[2]').send_keys("decide123456789@gmail.com")

        driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[3]').click()
        
        verification = str(driver.find_element_by_xpath('/html/body/div/section/div[2]/ul/li/div').text).startswith('El email ha sido enviado!')

        print('Criterio para test_enviar_email_correcto : ' + str(verification)) 

        driver.close()

        driver.quit()

def prueba_enviar_email_mal():

        driver = webdriver.Chrome(executable_path="./chromedriver_ubuntu")

        driver.get("http://127.0.0.1:8000/visualizer/1/")

        driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[2]').send_keys("emailmal.com")

        driver.find_element_by_xpath('/html/body/div/section/div[2]/div[3]/form/input[3]').click()
        
        verification = driver.find_elements_by_xpath('/html/body/div/section/div[2]/ul/li/div').count('El email ha sido enviado!') is 0

        print('Criterio para test_enviar_email_mal : ' + str(verification)) 


        driver.close()

        driver.quit()

def prueba_porcentaje():
 driver = webdriver.Chrome(executable_path="./chromedriver_ubuntu")
 driver.get("http://localhost:8000/visualizer/3")
 element = (driver.find_element_by_xpath("/html/body/div/section/div[2]/div[2]/p/p2[1]"))
 verification = (element.text).startswith('0')
 
 print("prueba de que salen los porcentajes :  " +  str(verification) )


def prueba_porcentaje_mal():
 driver = webdriver.Chrome(executable_path="./chromedriver_ubuntu")
 driver.get("http://localhost:8000/visualizer/3")
 element = (driver.find_element_by_xpath("/html/body/div/section/div[2]/div[2]/p/p2[1]"))
 verification = (element.text).startswith(' ')
 
 print("prueba de que no se ven los porcentajes : " +  str(verification) )

	
#prueba_porcentaje()  
#prueba_porcentaje_mal() 
#pruebaPDFCSV()
#prueba_enviar_email_correcto()
#prueba_enviar_email_mal()





