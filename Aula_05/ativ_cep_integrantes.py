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
with open(nome_arquivo, "w") as arquivo:   # with open(nome_arquivo, "w") as arquivo: Abre o arquivo especificado por nome_arquivo em modo de escrita ("w"). O uso de with garante que o arquivo será fechado automaticamente após o bloco de código ser executado, mesmo que ocorra uma exceção.
    for nome, cep in integrantes.items():   # Itera sobre os itens do dicionário integrantes. Cada item é uma tupla contendo um nome e um CEP. A função items() retorna essas tuplas de chave-valor do dicionário.
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")   # Faz uma requisição GET à API do ViaCEP, usando o CEP da iteração atual para obter os dados do endereço em formato JSON.
        dados = response.json() # Converte a resposta da API de JSON para um dicionário Python, permitindo o acesso aos dados do endereço de forma estruturada.
        cidade = dados.get("localidade", "Cidade não encontrada")  # Obtém o valor associado à chave "localidade" no dicionário dados. Se a chave não existir, retorna "Cidade não encontrada" como valor padrão.
        arquivo.write(f"Nome: {nome}, Cidade: {cidade}\n")  # Escreve uma linha no arquivo com o nome e a cidade obtida, formatada como uma string
        print(f"Nome:{nome}, Cidade: {cidade}")  # Exibe no console o nome e a cidade para cada iteração. Isso ajuda a verificar se o processo está funcionando corretamente durante a execução.
print(f"Dados salvos em {nome_arquivo}")  # Após a conclusão do loop e fechamento do arquivo, imprime no console uma mensagem indicando que os dados foram salvos no arquivo especificado.