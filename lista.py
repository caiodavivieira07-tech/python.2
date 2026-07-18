nomes = ["joão","Ana","Bruno"] #array, matriz ou vetor
print(f"Listagem de nomes {nomes}")
nomes.append("Carlos")
print(f"Listagem de nomes ATUALIZAADA {nomes}")
n=input("Digite um nome a ser excluido => ")
nomes.remove(n)
print(f"Listagem de nomes ATUALIZADA Exclusão {nomes}")
