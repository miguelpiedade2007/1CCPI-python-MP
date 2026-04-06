while True:
    resposta = input("quer continuar, ou deseja sair (s/sair)").lower().strip()

    if resposta == "s":
        print("olá mundo")
    elif resposta == "sair":
        print("fechando programa")
        exit()
    else:
        print("opção não registrada")


