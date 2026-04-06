idade = int(input("qual sua idade? "))

if idade < 16:
    print("você não pode votar!")
elif 18> idade >= 16:
    print("você pode votar")
elif 70> idade >= 18:
    print("você deve votar")
elif idade >= 70:
    print("você pode votar")