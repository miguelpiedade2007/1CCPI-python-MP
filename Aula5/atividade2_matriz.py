matriz = []
contador = 0
for i in range(4):
    linha = []
    for j in range(5):
        contador += 1
        linha.append(contador)
    matriz.append(linha)

for linha in matriz:
    print(linha)
#aqui é para acessar um elemnto específico
print()
print((matriz[1][2]))
