
soma = 0

n = int(input("Digite um número positvo N, esse programa exibirá a soma de todos os números até N: "))
while n%2 != 0:
    n = int(input("Por favor digite um número positivo: "))

else:
    for x in range(0, n+1,):
        soma += x
    print(f"A soma dos valores de 0 a {n} é de: {soma}")

