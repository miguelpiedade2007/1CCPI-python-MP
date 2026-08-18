#Uma API possui três endpoints, para valores entre 200 e 299 deve dar sucesso

endpoints = ["/login",  "/produtos", "/pedidos"]
status = [[200, 200, 401, 200, 500],
             [200, 200, 200, 200, 200,],
             [201, 500, 502, 201, 500]]

def porcentagem(lista_status):
    cont = 0
    for stat in lista_status:
        if stat > 299 or stat < 200:
            cont += 1
    porc = (len(lista_status) - cont)*100/len(lista_status)
    return porc

def mais_erros(lista_status, lista_endpoints):
    pior_percentual = 101
    pior_endpoint = 0

    for i, stat in enumerate(lista_status):
        if porcentagem(stat) < pior_percentual:
            pior_percentual = porcentagem(stat)
            pior_endpoint = lista_endpoints[i]
    return pior_endpoint

def erros_seguidos(lista_status):
    for i in range(len(lista_status)-1):
        if lista_status[i] > 299 and lista_status[i+1] > 299:
            return True

    return False

def classificacao(lista_status):
    if erros_seguidos(lista_status):
        return "Crítico"
    elif porcentagem(lista_status) < 80:
        return "Instável"
    else:
        return "Estável"

for i in range(len(endpoints)):
    nome = endpoints[i]

    print("-"*30)
    print(f"endpoint {i+1}:")
    print(classificacao(status[i]),":", porcentagem(status[i]))
print("-"* 30)
print("Endpoint com mais erros:", mais_erros(status, endpoints) )

























