import math
# y = 0
# n = int(input("DIgite um número positivo: "))
# for x in range(1, n+1):
#     y = n%x
#     if y == 0:
#         print(x)

# Determine e mostre todos os números primos no intervalo de 2 a 2000.
# Dicas:
# ▪ Para resolver esse problema, primeiro faça um algoritmo que verifica se um número inteiro qualquer é
# primo ou não.
# ▪ A seguir, com esse código em mãos, faça os ajustes necessários para mostrar todos os números primos
# no intervalo solicitado.
# ▪ Você precisará colocar uma estrutura de repetição dentro da outra.
# ▪ Laços aninhados!!!!



for x in range(2, 2000+1):
    eh_primo = True
    for y in range(2, math.isqrt(x)+1):
        if x % y == 0:
            eh_primo = False
            break
    if eh_primo:
        print(x)




