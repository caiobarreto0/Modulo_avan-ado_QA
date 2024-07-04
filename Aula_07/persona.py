from faker import Faker
import pandas as pd

fake = Faker('pt_BR')





def create_persona(number_of_personas: int)-> dict:
    personas_list = []
    
    

    for i in range(number_of_personas):
        data = {
    "nome" : fake.name(),
    "cidade" : fake.city(),
    "idade" : fake.random_int(18,100)
    }
    personas_list.append(data)

    return personas_list


lista_de_personas = create_persona(20)

df_lista_de_personas = pd.DataFrame(lista_de_personas)
print(df_lista_de_personas)

df_lista_de_personas.to_csv('lista_de_personas.csv', index=False)

