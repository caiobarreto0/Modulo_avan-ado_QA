import requests
import json
from faker import Faker

fake = Faker('pt_BR')

criar_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/"

login_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/login/"

data_usuario = {
    "username" : fake.user_name(),
    "email" : fake.email(),
    "password" : fake.password(),
    "phone" : fake.phone_number(),
    "cpf" : fake.ssn(),
    "address" : fake.address()
}


response = requests.post(criar_usuario, json=data_usuario)
if response.status_code == 201:
    print("Usuário criado com sucesso")
else:
    print(f"Falha ao criar usuário: {response.status_code}")
    print(response.json())


login_data ={
    "email" : data_usuario["email"],
    "password" : data_usuario["password"]
}

response = requests.post(login_usuario, json=login_data)
if response.status_code == 200:
    print("Login realizado com sucesso")
    login_response = response.json()



    with open("login_response.json", "w") as file_json:
        json.dump(login_response, file_json, indent=4)
    print("Resposta do login salva em 'login_response.json'.")
else:
    print(f"Falha ao realizar login: {response.status_code}")
    print(response.json())