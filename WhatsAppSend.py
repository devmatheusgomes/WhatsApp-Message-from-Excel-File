import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import easygui as ed
import pandas as pd
import random


# Selecionando Planilha de Clientes
planilha = ed.fileopenbox()
contatos_df = pd.read_excel(planilha)

#abrindo navegador e site pelo profile principal do usuario
Options = webdriver.ChromeOptions()
#Altere aqui o caminho para o seu profile do chrome
Options.add_argument(r"--user-data-dir=c:\users\Matheus Gomes\AppData\Local\Google\Chrome\User Data")
#Altere aqui para o caminho do seu chromedriver
navegador = webdriver.Chrome(executable_path=r'c:\WebDriver\chromedriver.exe', chrome_options=Options)

navegador.get("https://web.whatsapp.com/")

#Esperando abrir janela de conversas do whatsapp
navegador.find_elements(By.ID, "side")
time.sleep(10)

#Lendo planilha e enviando mensagens
for i, razaos in enumerate(contatos_df['Razao']):
    razaosocial = contatos_df.loc[i, "Razao"]
    numero = contatos_df.loc[i, "Numero"]
    texto = urllib.parse.quote(f"Bom dia, a respeito da empresa {razaosocial}, ")
    link = f"https://web.whatsapp.com/send?phone=+55{numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(random.randrange(5, 8))

        #Validando Numero do WhatsApp, se for verdadeira, envia mensagem
        if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
            #Enviando mensagem com numero valido
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
            time.sleep(2)
            #Avisando o Usuario do Numero Invalido com os dados
        else: ed.msgbox(msg=f"O Número {numero} da Empresa {razaosocial} é Inválido", ok_button="Continuar")

#fechando navegador aberto
navegador.quit()
ed.msgbox(msg="PROCESSO FINALIZADO", ok_button='OK', title='FIM')

