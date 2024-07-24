from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('que estou na página do Instituto Joga Junto')
def etapa_acessar_pagina(context):
    context.browser = webdriver.Firefox()
    context.browser.get('https://www.jogajunto.com.br/')

    titulo_pagina = context.browser.title
    assert 'Instituto Joga Junto' in titulo_pagina, "Título da página não encontrado (esperava 'Instituto Joga Junto')"


@when('preencho o formulário de contato')
def etapa_preencher_formulario(context):
    input_name = context.browser.find_element(By.NAME, 'nome').send_keys('Caio')
    input_email = context.browser.find_element(By.NAME, 'email').send_keys('caio@gmail.com')
    input_descp = context.browser.find_element(By.NAME, 'body').send_keys('Automação final')

@when('aperto o botão de enviar')
def etapa_clicar_botao_enviar(context):
    botao_enviar = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Enviar")]')))
    ActionChains(context.browser).move_to_element(botao_enviar).click().perform()


@then('os dados são recebidos com sucesso')
def etapa_verificar_envio(context):
    mensagem_sucesso = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Mensagem enviada com sucesso")]')))
    assert 'Mensagem enviada com sucesso' in mensagem_sucesso.text, "Mensagem de sucesso não encontrada (esperava 'Mensagem enviada com sucesso')"
    context.browser.quit()



    