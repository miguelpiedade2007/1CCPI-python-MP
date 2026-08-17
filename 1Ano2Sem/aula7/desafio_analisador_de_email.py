#Desafio analisador de emails da Fiap
#lucas.mendes@fiap.com.br, camila.rocha@gmail.com, lucas.mendes@yahoo.com, beatriz.lima@fiap.com.br
emails = input("Digite os emails separados por vírgulas: ").split(",")

dominio = dict()
for email in emails:
    email_limpo = email.strip()
    user, dom = email_limpo.split("@")

    for d in dom:
        if d not in dominio:
            dominio[dom] = 1
        else:
            dominio[dom] += 1

print("Domínios:")
print(dominio)




