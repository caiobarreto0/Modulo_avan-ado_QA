valor_compra = float(input("Digite o valor total da compra: "))

if valor_compra > 500.00:
    print("Parabéns. você ganhou um super desconto de 30%")
elif valor_compra >= 250.00:
    print("Parabéns. você ganhou 10% de desconto, mas pode ganhar 30% se sua compra for acima de R$500,00")
else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")