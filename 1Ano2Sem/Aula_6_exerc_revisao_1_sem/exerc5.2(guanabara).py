
# Receber um núemro e verificar se é primo
# printar todos os números até esse recebido / Acabei modificando essa regra pra deixar mais otimizado, será printado apenas até metade de N
# indicando se são primos ou não










n = int(input("Dale: "))
count = 0
for x in range(1, int(n/2)+1):
    if n % x == 0:
        count += 1
        print(f"{x} divisor")
    else:
        print(f"{x} não divide")
    if count >= 2:
        break


if count >= 2:
    print("o número não é primo")


elif n == 1:
    print("o número não é primo")

else:
    print("o número é primo")
