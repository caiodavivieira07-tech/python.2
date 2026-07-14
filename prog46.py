total = 0 

while True:
    print("\Tabela de Produtos")
    print("001 -> Arroz - R$ 4")
    print("002 -> Feijão - R$ 7")
    print("003 -> Macarrão - R$ 5")
    print("0 -> Finalizar")

    codigo = input("Digite o código do produto:")

    if codigo == "001":
        print("Produto adicionado: Arroz - R$ 4")
        total += 4

    elif codigo == "002":
        print("Produto adicionado: Feijão - R$ 7")
        total += 7
    
    elif codigo == "003":
        print("Produto adicionado: Macarrão - R$ 5")
        total += 5
    
    elif codigo == "0":
        break

    else: 
        print("Código inválido!")

    print("Total parcial: R$" , total)

print("Compra finalizada!")
print("Total da compra: R$" , total)