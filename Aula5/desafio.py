lista_nomes = ["Ana", "Lara", "Luiz", "Caio"]


for i in range(len(lista_nomes)):
    for j in range(i + 1, len(lista_nomes)):
        print(lista_nomes[i], lista_nomes[j])
        print(i, j)
