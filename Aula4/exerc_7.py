n = int(input("digite um valor positivo: "))
resultado = 0

if n % 2 == 0:
    for x in range(1, n+1):
        resultado = resultado + x

else:
    print("valor não é par")



print(f"a soma dos valores de 1 a {n} é {resultado}")


