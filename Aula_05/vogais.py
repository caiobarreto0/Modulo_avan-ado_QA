palavra = input("Informe uma plavra: ")
vogais = 'aeiou'
contador = 0

for i in palavra:
    if i in vogais:
        contador   += 1
print(f"O número total de vogais na palavra '{palavra}' é: {contador}")