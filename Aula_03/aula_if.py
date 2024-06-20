
# time = input("Digite o seu time: ")

# if time == 'Corinthians':
#     print("Você é um timão")
# elif time == "Bahia":
#     print("Você é do Esquadrão")
# else:
#     print("Você não é um timão")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Cidadão possui idade mínima para dirigir")
elif 17 <= idade < 18:
    print("Indivíduo tem entre 17 e 18 anos e ainda não está apto para dirigir")
else:
    print("Cidadão não possui idade mínima para dirigir")
