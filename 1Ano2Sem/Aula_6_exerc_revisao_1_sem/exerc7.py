
vetor = []

n = int(input("Digite um número: "))

for i in range(1, n+1):
    m = input("Digite uma letra: ")
    vetor.append(m)

# for letras in reversed(vetor):
#     print(letras)

# OU:

print(vetor[::-1])