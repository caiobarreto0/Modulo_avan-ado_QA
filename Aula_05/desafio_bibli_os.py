import os

dados = ["The last of us", "Dead Space", "The Calisto Protocol", "FC 24"]

# Variavel com o nome do diretório 
diretorio = "Desafio_OS"

# Comando para criar o diretório (O parâmetro 'exist_ok=True' impede que ocorra um erro se o diretório já existir.)
os.makedirs(diretorio, exist_ok=True)

# Criar nome do arquivo
nomeArquivo = os.path.join(diretorio, "dados.txt")

# Abrir o arquivo no modo escrita e escreve os dados
with open(nomeArquivo, "w") as arquivo:
    for linha in dados:
        arquivo.write(linha + "\n")

print(f"Dados salvos em {nomeArquivo}")

