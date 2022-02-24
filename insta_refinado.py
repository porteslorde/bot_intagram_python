from ast import Try
from gettext import find
from lib2to3.pgen2 import driver
from logging import exception
from xml.dom.minidom import Element
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random

class robozao:
    def __init__(self,username,senha):
        self.username = username
        self.senha = senha
        self.driver = webdriver.Chrome(r'digite aqui o local do chromedriver.exe')

    def login (self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        usuario = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        usuario.click()
        usuario.send_keys(self.username)
        time.sleep(2)
        senha = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        senha.click() 
        senha.send_keys(self.senha)
        time.sleep(2)
        entrar = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        entrar.click()
        time.sleep(4)
        self.perfis('Digite aqui a hash que deseja sem #')
        
      
    
    def perfis (self,perfil):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+perfil+'/')
        time.sleep(2)
        abrir_img = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        abrir_img.click()
        time.sleep(3) 
    
        
        try:
                 for i in range(1,2):
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    time.sleep(2)

                    fotos = driver.find_elements_by_tag_name('a')
                    link_fotos = [elem.get_attribute('href') for elem in fotos]
                    [href for href in link_fotos if perfil in href]
                    time.sleep(4)

                   
                 for repetir in link_fotos:
                    driver.get(repetir)
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') 
                    time.sleep(2)
            
                    curtir = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')
                    curtir.click()
                    time.sleep(4)

        finally:
            return print('Fim.')

           
            

startbot = robozao ('Digite aqui seu usuario','Digite aqui sua senha')
startbot.login()

