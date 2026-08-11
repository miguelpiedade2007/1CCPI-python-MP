y = 0
n = int(input("DIgite um número positivo: "))
for x in range(1, n+1):
    y = n%x
    if y == 0:
        print(x)

