senha correta = "python123"
tentativas = 0
max tentativas

while tentativas < max tentativas:
    tentativa = input(f"Digite a senha(Tentativa{tentativas + 1}/ {max tentativas}):")
    if tentativa == senha correta:
        print("Acesso concedido! Bem-vindo.")
        break
    else:
        print("Senha_incorreta.")
        tentativas += 1
else:
    print("Você excede o número máximo de tentativas. Acesso bloqueado.")
