print("Todos os números primos de 2 a 2000")

for x in range(2, 2001):
    primo = True
    for i in range(2, x//2 + 1):
        if x % i ==0:
            primo = False
            break


    if primo:
        print(x)




