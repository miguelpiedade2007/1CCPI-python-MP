def print_lyrics():
    print("oh we're half way there")
    print("oh-oh ohh Livin' on a prayer")

print_lyrics()
print_lyrics()

print(print_lyrics)
print(type(print_lyrics))




#if e else:

nota = float(input("qual sua nota?"))
if nota <= 6:
    print("voce está reprovado")
else:
    print("voce passou")

#if e else com encadeamento:

nota2 = float(input("qual sua nota?"))
if nota2 <= 4:
    print("voce está reprovado")
else:
    if nota2 <= 6:
        print("você está de recuperação")
    else:
        print("aprovado")


#if e else e elif
nota3 = float(input("qual sua nota"))
if nota3 <=4:
    print("voce está reprovado")
elif 6 > nota3 > 4:
    print("você está de recuperação")
elif nota3 >= 6:
    print("voce passou")


