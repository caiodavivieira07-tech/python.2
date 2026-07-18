carros = []
contador = 0
while contador < 3:
    carro = input("Digite o nome do carro: ")
    carros.append(carro)
    contador += 1
print("Lista de carros:")
for carro in carros: 
    print(carro)
