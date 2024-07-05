import requests
import json

criar_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/"
login_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/login/"





data_user = {
    "username": "grilo",
    "password": "123456789012",
    "email": "grilo@gmail.com",
    "cpf": "03576300502",
    "phone": "71982080540",
    "address": "123 Main St, city, Country"
}

response = requests.post(criar_usuario, json=data_user)
if response.status_code==201:
    print("Usuário criado com sucesso")
else:
    print(f"Erro ao criar usuário {response.status_code}")
    print(response.json())


    login_user = {
        "email": data_user["email"],
        "password": data_user["password"]
    }


    response = requests.post(login_usuario, json=login_user)
    if response.status_code==200:
        print("Usuário logado com sucesso")
        login_response = response.json()


        with open("login_response", "w") as file_json:
            json.dump(login_response, file_json, indent=4)
        print("Resposta salva em 'login_response.json'.")
    else:
        print(f"Erro ao logar usuário {response.status_code}")
        print(response.json())