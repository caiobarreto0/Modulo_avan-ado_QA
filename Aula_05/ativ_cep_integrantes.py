import requests
import os

# Criar estrutura de dicionário com nome e cep dos integrantes da squad
integrantes = {
    "Caio": "41194-105",
    "Anniele": "44400-000",
    "Vitor Back": "52031-244",
    "Julia Robaina": "74333-040",
    "Tamires": "58416-389",
}

# Criar um diretório para salvar o arquivo de texto

diretorio = 'cep squad'
os.makedirs(diretorio, exist_ok=True)

# Abre um arquivo para salvar os dados dos integrantes
nome_arquivo = os.path.join(diretorio, "cep_integrantes.txt")
with open(nome_arquivo, "w") as arquivo:
    for nome, cep in integrantes.items():
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = response.json()
        cidade = dados.get("localidade", "Cidade não encontrada")
        arquivo.write(f"Nome: {nome}, Cidade: {cidade}\n")
        print(f"Nome:{nome}, Cidade: {cidade}")
print(f"Dados salvos em {nome_arquivo}")