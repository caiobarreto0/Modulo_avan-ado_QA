import os
import requests

integrantes = [
    {"Integrante": "Caio", "CEP": "41194-105"},
    {"Integrante": "Anielle", "CEP": "58200-000"},
    {"Integrante": "Julia", "CEP": "25268-160"},
    {"Integrante": "Tamires", "CEP": "07179-260"},
    {"Integrante": "Vitor", "CEP": "79009-080"},
]

diretorio = 'cep_squad'
os.makedirs(diretorio, exist_ok=True)

nome_arquivo = os.path.join(diretorio, 'cep_integrantes.txt')
with open(nome_arquivo, 'w') as arquivo:
    for integrante in integrantes:
        nome = integrante['Integrante']
        cep = integrante['CEP']
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = response.json()
        cidade = dados.get("localidade", "Cidade não encontrada")
        arquivo.write(f'Nome: {nome}, Cidade: {cidade}\n')
        print(f'Nome: {nome}, Cidade: {cidade}')
print(f'Arquivo salvo em: {nome_arquivo}')