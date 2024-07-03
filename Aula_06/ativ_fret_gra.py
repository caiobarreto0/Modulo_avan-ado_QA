import requests

norte_nordeste = ["AC", "AP", "AM", "PA", "RO", "RR", "TO", "AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]

def cep_estado (cep):
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        response.raise_for_status() 
        dados = response.json() 
        return dados.get("uf")
    except (requests.RequestException,ValueError): 
        return None
    

def frete_gratis(cep, valor_compra):
    
    estado = cep_estado(cep)
    if estado:
        if estado in norte_nordeste:
            if valor_compra >= 100:
                return f"Compra de R${valor_compra:.2f}. CEP {cep} - Estado: {estado}. VOCÊ É ELEGÍVEL PARA FRETE GRÁTIS!"
            else:
                return f"Compra de R${valor_compra:.2f}. CEP {cep} - Estado: {estado}. O valor da compra é insuficiente para frete grátis."
        else:
             return f"CEP {cep} - Estado: {estado}. Infelizmente, o frete grátis não está disponível para sua região."
    else:
        return "CEP inválido ou não encontrado"
        
    

def main():
   cep = input("Digite o CEP (apenas números): ").strip()

   try:
       valor_compra = float(input("Digite o valor da compra: ").strip())
   except ValueError:
       print("Valor inválido")
       return
   
   if len(cep) == 8 and cep.isdigit():
       print(frete_gratis(cep, valor_compra))
   else:
        print("Formato de CEP inválido. O CEP deve conter 8 dígitos numéricos")

if __name__ == "__main__": 

    main()
         
