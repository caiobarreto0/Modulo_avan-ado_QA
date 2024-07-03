import pandas as pd

df = pd.read_csv('dados_ficticios.csv')

filtro_idade = df[df['idade']> 40]

filtro_renda_5mil = df[df['renda'] > 5000]

filtro_renda_15mil = df[df['renda'] > 15000]

print("Pessoas com idade maior que 40 anos: ")
print(filtro_idade)

print("\nPessoas com renda maior que 5 mil: ")
print(filtro_renda_5mil)

print("\nPessoas com renda maior que 15 mil: ")
print(filtro_renda_15mil)