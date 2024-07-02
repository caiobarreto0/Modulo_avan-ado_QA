matricula = int(input('Digite o numero da sua matricula: '))

def par_impar(matricula):
    if matricula % 2 == 0:
        print('VOCÊ ESTÁ NO TIME AZUL')
    else:
        print('VOCÊ ESTÁ NO TIME AMARELO')

par_impar(matricula)