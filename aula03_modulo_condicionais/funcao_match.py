escolha_usuario = 0
# 0 = sai
# 1 = entra

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar no programa")
    case _:
        print("erro")