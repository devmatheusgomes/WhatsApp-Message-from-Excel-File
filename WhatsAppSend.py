import urllib.parse
from selenium import webdriver
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
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\mathe\AppData\Local\Google\Chrome\User Data")
navegador = webdriver.Chrome(executable_path=r'C:\Path\chromedriver.exe', chrome_options=options)
>>>>>>> master
navegador.get("https://web.whatsapp.com/")

# esperando abrir conversas
while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(10)

# lendo planilha e enviando menasgns
for i, razaos in enumerate(contatos_df['Razao']):
    razaosocial = contatos_df.loc[i, "Razao"]
    numero = contatos_df.loc[i, "Numero"]
    texto = urllib.parse.quote(f"Bom dia, a respeito da empresa {razaosocial}, ")
    link = f"https://web.whatsapp.com/send?phone=+55{numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(random.randrange(10, 15))
    try:
        navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(random.randrange(5, 13))
    except Exception:
        pass

ed.msgbox(msg="PROCESSO FINALIZADO", ok_button='OK')

