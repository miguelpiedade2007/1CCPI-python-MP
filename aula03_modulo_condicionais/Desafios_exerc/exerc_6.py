print("Programa: calculadora")
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
operacao = input("qual operação desejada? (+, *, /, -) ")

if operacao == "+":
    resultado = num1 + num2
    print(f"resultado: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"resultado: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"resultado: {resultado}")
elif operacao == "/":
    resultado = num1 / num2
    print(f"resultado: {resultado}")