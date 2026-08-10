t = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
print(t)
print(type(t))


t = tuple("Fiap")
print(t)
print(t[1])
print(t[1:3])

print()

u = ("F",) + t[1:]
print(u)

#Atribuição com Tuplas
print()
a = 5
b = 10
print(f"a: {a}, b: {b}")

print()
temp = a
a = b
b = temp
print(f"a: {a}, b: {b}")
print()

a, b = b, a
print(f"a: {a}, b: {b}")

email = "fulano@gmail"
usuario, dominio = email.split("@")
print(f"usuario: {usuario}, dominio: {dominio}")
