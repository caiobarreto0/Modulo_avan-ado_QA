num = int(input('Digite um numero qualquer'))

print(f'Tabuada de {num}:')
for i in range(1,11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')