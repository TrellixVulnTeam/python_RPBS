nivel = input("Digite o nível de acesso: ").upper()

if nivel == "ADM" or nivel == "USR":
    genero = input("Digite o seu gênero: ").upper()
    if nivel == "ADM":
        if genero == "MASCULINO":
            print("Olá administrador")
        else:
            print("Olá administradora")
    else:
        if genero == "MASCULINO":
            print("Olá usuário")
        else:
            print("Olá usuária")
elif nivel == "GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido")
