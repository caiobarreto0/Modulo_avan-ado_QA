##language: pt

Feature: Enviar formulário de contato no site do Instituto Joga Junto

  cenario: Enviar formulário de contato com sucesso
    Dado que estou na página do Instituto Joga Junto
    Quando preencho o formulário de contato
    E aperto o botão de enviar
    Então os dados são recebidos com sucesso
 