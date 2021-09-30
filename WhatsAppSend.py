import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import easygui as ed
import pandas as pd
import random

#Selecionando Planilha de Clientes
planilha = ed.fileopenbox()
contatos_df = pd.read_excel(planilha)

#abrindo navegador e site
navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')

#esperando abrir conversas
while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(10)

#lendo planilha e enviando menasgns
for i, razaos in enumerate(contatos_df['Razao']):
    razaosocial = contatos_df.loc[i,"Razao"]
    numero = contatos_df.loc[i, "Numero"]
    texto = urllib.parse.quote(f"Bom dia, a respeito da empresa {razaosocial}, Matheus da Consult aqui, estou entrando em contato para atualizarmos o seu sistema, me passa o ID do computador por gentileza!")
    link = f"https://web.whatsapp.com/send?phone=+55{numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(random.randrange(10, 20))
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(15)
ed.msgbox(msg="PROCESSO FINALIZADO")









