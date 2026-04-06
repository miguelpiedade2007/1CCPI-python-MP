salario = float(input("qual seu salario? "))
if 280>= salario:
    novo_valor = salario * 0.20
    reajuste = salario + 0.20 * salario
    aumento = "20%"

elif  700 >= salario > 280:
    novo_valor = salario * 0.15
    reajuste = salario + 0.15 * salario
    aumento = "15%"

elif 1500 > salario > 700:
    novo_valor = salario * 0.10
    reajuste = salario + 0.10 * salario
    aumento = "10%"

elif 1500 >= salario:
    novo_valor = salario * 0.05
    reajuste = salario + 0.05 * salario
    aumento = "5%"

print(f"seu salário é:{salario}")
print(f"o percentual de aumento foi  de {aumento}")
print(f"o valor de aumento foi de: {novo_valor}")
print(f"valor reajustado: {reajuste}")