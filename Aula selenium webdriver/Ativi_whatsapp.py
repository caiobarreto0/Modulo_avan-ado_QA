
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Configuração do WebDriver (use o caminho correto para o seu driver)
driver = Firefox()  # Ou Firefox() se você preferir

# Acessar o WhatsApp Web
driver.get('https://web.whatsapp.com')

# Aguardar o usuário escanear o QR code (tempo suficiente para escanear)
print("Por favor, escaneie o QR code para acessar o WhatsApp Web.")
WebDriverWait(driver, 120).until(  # Tempo de espera de 120 segundos
    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
)


def enviar_mensagem(contato, mensagem):
    
    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    search_box.clear()  
    search_box.send_keys(contato)
    time.sleep(2)  

    
    try:
        contact = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//span[@title="{contato}"]'))
        )
        contact.click()
    except:
        print(f"Contato '{contato}' não encontrado.")
        return  

   
    message_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
    )

   
    for letter in mensagem:
        message_box.send_keys(letter)
        time.sleep(0.1) 

   
    message_box.send_keys(Keys.ENTER)
    print(f"Mensagem enviada para '{contato}'.")


enviar_mensagem("[TA 1/2024] QA MÓDULO AVANÇADO", "Automação do WhatsApp - Baygon Quality")


time.sleep(5)
driver.quit()
