maior = 0

for x in range (5):
    num = float(input(f"digite o {x + 1} número: "))
    if num > maior:
        maior = num

print(f"o maior número é {maior}")