import math
e_primo = 1
for x in range(2, 2000):
    for y in range(2,x-1):
        if x % y == 0:
            primo = False
            break


        if e_primo == True:
            print(x)
