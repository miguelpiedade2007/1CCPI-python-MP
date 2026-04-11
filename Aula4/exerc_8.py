n = int(input("Digite um valor positivo: "))
while n % 2 != 0:
    print("o valor não é par")
    n = int(input("Digite um valor positivo: "))

print(f"os divisores de 1 a {n}")
for x in range (1, n+2):
    if n % x == 0:
        if n ==x:
            print(x)
        else:
            print(x, end=",")
