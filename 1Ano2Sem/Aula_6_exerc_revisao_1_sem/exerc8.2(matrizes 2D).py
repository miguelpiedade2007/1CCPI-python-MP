#Igual o 8 mas será com matrizes de duas dimensões

A = [[-3, 7, 5],
     [5, 11, 10]]

B = [[4, -5, -2],
     [-1, -6, -4]]

C = []

for i in range(len(A)):
    D = []


    for x in range(len(A[0])):
        m = A[i][x] + B[i][x]
        D.append(m)

    C.append(D)





print(C)


