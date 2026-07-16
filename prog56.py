def situacao(n1,n2,n3,n4):
    media=(n1+n2+n3+n4)/4
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
n1=float(input("Digite a nota 1 "))
n2=float(input("Digite a nota 2 "))
n3=float(input("Digite a nota 3 "))
n4=float(input("Digite a nota 4 "))
situacao(n1,n2,n3,n4)
