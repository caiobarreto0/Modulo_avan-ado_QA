from faker import Faker
import random

fake = Faker('pt_br')

nome = fake.name()
cidade = fake.city()
idade = random.randint(18,80)

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cidade: {cidade}")