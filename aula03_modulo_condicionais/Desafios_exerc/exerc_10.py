print("Classificação de triângulos")

A = float(input("Digite a medida de um dos lados: "))
B = float(input("Digite a medida de um dos lados: "))
C = float(input("Digite a medida de um dos lados: "))

A, B, C= sorted([A, B, C], reverse=True)


if A >= B + C:
    print("os lados não formam um triângulo")
else:
    if A * A == B * B + C * C:
        print("triângulo retângulo")


    elif A * A > B * B + C * C:
        print("triângulo obtuso")

    elif A * A < B * B + C * C:
        print("triângulo agudo")
