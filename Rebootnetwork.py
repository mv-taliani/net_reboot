import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
# Abrir o Navegador e fazer Login

driver = Chrome()
driver.get('http://192.168.1.1')
# Logar dentro do Roteador
driver.find_element(By.XPATH, r'//*[@id="Frm_Username"]').send_keys("multipro")
driver.find_element(By.XPATH, r'//*[@id="Frm_Password"]').send_keys("multipro")
# Navegar nas opcoes
driver.find_element(By.XPATH, r'//*[@id="LoginId"]').click()

time.sleep(2)

# iframe = driver.find_element(By.XPATH, r'//*[@id="Fnt_mmManager"]')
driver.switch_to.frame('mainFrame')
driver.find_element(By.XPATH, r'//*[@id="Fnt_mmManager"]').click()
driver.find_element(By.XPATH, r'//*[@id="smSysMgr"]').click()
driver.find_element(By.XPATH, r'//*[@id="Submit1"]').click()
driver.find_element(By.XPATH, r'//*[@id="msgconfirmb"]').click()
time.sleep(2)



# Acessar a Guia Chamadas para exportar os relatorios




