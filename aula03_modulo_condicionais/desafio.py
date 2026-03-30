print("veja se você pode votar!!!!")
idade = int(input("qual sua idade? "))

if idade < 16:
    print("você não pode votar!")
elif 18> idade >= 16:
    print("você pode votar")
elif idade >= 18:
    print("você deve votar")