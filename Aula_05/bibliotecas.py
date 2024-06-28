# import requests

# cep = input ('Qual seu cep')

# response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

# data = response.json()

# print(f'O logadouro dessa chamada é', data['logradouro'])

import requests

# Solicita o CEP ao usuário
cep = input('Qual seu CEP: ')

# Faz a requisição à API ViaCEP
response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

# Verifica se a resposta da API foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    
    # Verifica se o CEP é válido
    if 'erro' not in data:
        print(f'O logradouro dessa chamada é: {data["logradouro"]}')
    else:
        print('CEP inválido.')
else:
    print('Não foi possível obter os dados do CEP.')
