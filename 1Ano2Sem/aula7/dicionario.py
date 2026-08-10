eng2esp = dict()
print(eng2esp)

eng2esp["one"] = "uno"
print(eng2esp)

eng2esp= {"one": "uno",
        "two": "dos",
        "three": "tres"
}
print(eng2esp["two"])

print(len(eng2esp))

#Operador in
print("uno" in eng2esp)

#valores
valores_dict = eng2esp.values()
print("uno" in valores_dict)


#exercício contador de letras:
print()
def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("ana")
print(dict_contagem)