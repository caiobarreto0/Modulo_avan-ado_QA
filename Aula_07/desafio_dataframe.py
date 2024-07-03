import pandas as pd

dados ={
    'Nome': ['Anielle', 'Caio', 'Vitor Back', 'Tamires', 'Julia', 'João', 'Maria'],
    'Idade': [20, 36, 27, 30, 25, 30, 45],
    'Cidade': ['Recife', 'São Paulo', 'Recife', 'Recife', 'Salvador', 'Salvador', 'Manaus']
}

df = pd.DataFrame(dados)

moradores_recife = df[df['Cidade'] == 'Recife']

print(moradores_recife)