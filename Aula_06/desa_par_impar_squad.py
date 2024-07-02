def verificar_matricula(numero_matricula):
    if numero_matricula % 2 == 0:
        print(f"Número de matrícula {numero_matricula}: VOCÊ ESTÁ NO TIME AZUL")
    else:
        print(f"Número de matrícula {numero_matricula}: VOCÊ ESTÁ NO TIME AMARELO")


def main(): # Define a função main que será responsável pela lógica principal do script.
    lista_matriculas = [] # Inicializa uma lista vazia lista_matriculas para armazenar os números de matrícula inseridos pelo usuário.

    print("Por favor, insira até 5 números de matrícula.")

    while len(lista_matriculas) < 5: # Inicia um laço while que continua executando enquanto o comprimento da lista lista_matriculas for menor que 5.
        try: # Inicia um bloco try para tentar executar o código que pode gerar uma exceção (erro).
            numero = int(input(f"Digite o número da matrícula {len(lista_matriculas)+1}:"))
            lista_matriculas.append(numero) # Adiciona o número de matrícula à lista lista_matriculas.
        except ValueError:  # Captura a exceção ValueError que ocorre se a conversão de entrada para inteiro falhar 
            print("Por favor, insira um número válido")
    print("\nVerificando os grupos dos números de matrícula inseridos...\n")


    for numero in lista_matriculas: # Inicia um laço for que itera sobre cada número de matrícula na lista lista_matriculas.
        verificar_matricula(numero) # Para cada número de matrícula na lista, chama a função verificar_matricula passando o número como argumento.

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente (não importado como um módulo em outro script).
 main() # Se o script está sendo executado diretamente, chama a função main para iniciar o programa.