#Desafio de email, agora com tuplas
#lucas.mendes@fiap.com.br, camila.rocha@gmail.com, lucas.mendes@yahoo.com, beatriz.lima@fiap.com.br
emails = input("Digite os emails separados por vírgulas: ").split(",")
usuarios = []
dominio = dict()

for email in emails:
    email_limpo = email.strip()
    user, dom = email_limpo.split("@")
    usuarios.append(user)
    t_users = tuple(usuarios)



    for d in dom:
        if d not in dominio:
            dominio[dom] = 1
        else:
            dominio[dom] += 1

tupla_invertida = t_users[-1], * t_users[1:-1], t_users[0] #aqui não são necessários parênteses em elementos que buscam str[0]
# t invertida = (t_users[-1],) + t_users[1:-1] + (t_users[0],)   os () e , fazem ir de str para tupla

print("Quantidade de emails por domínio:")
print(dominio)
print("lista de usuários: ")
print(t_users)
print("Nova lista: ")
print(tupla_invertida)
