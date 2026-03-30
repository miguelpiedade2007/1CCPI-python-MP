verifica_email = True
verifica_senha = True
verifica_login = verifica_email and verifica_senha


if verifica_login is True:
    print("voce esta logado")
else: 
    print("login incorreto")