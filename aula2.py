from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get(r'C:\Users\Gabriel nery\Downloads\Arquivos\Pagina Hashtag.html')

navegador.find_element(By.XPATH, '//*[@id="header"]/div/div/div[1]/a/img').click()





