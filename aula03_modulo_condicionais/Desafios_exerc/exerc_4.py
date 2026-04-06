nota = float(input("qual sua nota"))
if nota < 5:
    print("voce está reprovado")
elif 7 > nota >= 5:
    print("você está de recuperação")
elif nota >= 7:
    print("voce passou")