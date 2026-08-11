import random

vetor = []



n = float(input("Digite o tamanho do vetor: "))

for x in range(1, int(n+1)):
    num = random.uniform(1, 20000)
    vetor.append(num)

print(vetor)

