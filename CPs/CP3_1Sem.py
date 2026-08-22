# Uma escola está testando um sistema simples de monitoramento ambiental
# para identificar salas com possível risco de calor excessivo.
# Você recebeu uma matriz em que cada linha representa uma sala
# e cada coluna representa a temperatura registrada em um horário diferente do dia.

# Saída esperada:
# Sala 1
# Média: 31.5
# Registros críticos: 2


temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]]
salaquente = 0
sala_maisquente = 0

for i, sala in enumerate(temperaturas):
    media = 0
    cont = 0
    for temperatura in sala:
         media += temperatura
         if temperatura >= 33:
             cont += 1



    print("-"*30)
    print(f"Sala {i + 1}")
    print(f"Média: {media/len(sala)}")
    print(f"Registros críticos: {cont}")

    if cont > salaquente:
        salaquente = cont
        sala_maisquente = i+1
print("-" *30)
print(f"Sala com maior risco: {sala_maisquente}")


