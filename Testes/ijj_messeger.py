from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def configurar_driver():
    
  
    driver = Firefox()
    return driver

def acessar_pagina(driver, url):
   
    driver.get(url)

def realizar_pesquisa(driver, query):
  
    search_box = driver.find_element(By.ID, "APjFqb")
    search_box.send_keys(query, Keys.ENTER)
    time.sleep(3)  

def clicar_no_link(driver, url):
   
    links = driver.find_elements(By.TAG_NAME, "cite")
    for link in links:
        if link.text == url:
            link.click()
            break

def preencher_formulario(driver, nome, email, assunto, mensagem):
   
    form = driver.find_element(By.TAG_NAME, "form")
    
    input_name = form.find_element(By.NAME, "nome")
    input_name.send_keys(nome)
    
    input_email = form.find_element(By.NAME, "email")
    input_email.send_keys(email)
    
    select_assunto = Select(form.find_element(By.NAME, 'assunto'))
    select_assunto.select_by_visible_text(assunto)
    
    textarea = form.find_element(By.NAME, "body")
    textarea.send_keys(mensagem)
    
    form.submit()

def main():
    
    driver = configurar_driver()

   
    url_google = "https://www.google.com/"
    acessar_pagina(driver, url_google)
    realizar_pesquisa(driver, "Instituto Joga Junto")

   
    url_instituto = "https://jogajuntoinstituto.org"
    clicar_no_link(driver, url_instituto)

    
    preencher_formulario(driver, "Teste Atividade Módulo Avançado", 
                         "testeatividademoduloavancado@gmail.com", 
                         "Me inscrever em um curso", 
                         "Teste Atividade Joga Junto")

    
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()
