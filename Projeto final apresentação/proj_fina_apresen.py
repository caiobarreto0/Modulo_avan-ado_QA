import requests
from faker import Faker
import json


BASEURL = "https://desafiopython.jogajuntoinstituto.org"
USERS = "users"
LOGIN = "login"
  
# Função para criar dados falsos de um usuário
def generate_user_data() -> dict:
    fake = Faker("pt_BR")
    data = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "cpf": fake.cpf()  
    }

    #para substituir a quebra de linha do endereço criado pela biblioteca faker por um hífen
    splitAddress = data["address"].split("\n")
    data["address"] = " - ".join(splitAddress)

    return data

def createUserAPI(user: dict ) -> None:
    try:
        response = requests.post(f"{BASEURL}/api/{USERS}/", data = user)
        #uma requisição malfeita (resposta que não tenha código 200), levanta uma exceção
        response.raise_for_status()
    #pega erros HTTP
    except requests.exceptions.HTTPError as error:
        print(f"Erro: {error}")
    else:
        print(f"Usuário criado com sucesso!")


def saveResponseJson(login_response: dict) -> None:
    try:
        with open("login_response.json", "w") as file_json:
            json.dump(login_response, file_json, indent = 4)
            print(f"Resposta do login salva em 'login_response.json'.")
    except IOError as error:
        print(f"Não foi possível salvar o seu arquivo: {error}")


def login_user(user_data: dict) -> None:

    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
   
    try:
        response = requests.post(f"{BASEURL}/api/{USERS}/{LOGIN}/", json=login_data)
        response.raise_for_status() 
    except requests.exceptions.HTTPError as error:
        print(f"Erro: {error}")
    else:
        saveResponseJson(response.json())



def main() -> None:
  user_data = generate_user_data()
  
  print(f"Os dados do usuário são")
  for key,value in user_data.items():
      print(f'{key}: {value}')
  
  createUserAPI(user_data)
  login_user(user_data)

if __name__ == "__main__": 

    main()
