frutas = ["maçã", "banana", "laranja", "uva", "morango"]

alergias = []

alergias.append(frutas[2])

for fruta in frutas:
    if fruta in alergias:
        print(f"Atenção você é alérgico a {fruta}")