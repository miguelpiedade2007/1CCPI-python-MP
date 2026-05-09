n = int(input("Qual o número de alunos? "))
soma_nota = 0
vetor_nota = []
acima_media = 0
igual_media = 0
abaixo_media = 0
for i in range(n):
    nota = int(input(f"Qual a nota do aluno {i +1} ? "))
    if nota > 10:
        print("erro")
        break
    elif nota < 0:
        print("erro")
        break
    vetor_nota.append(nota)
    soma_nota += nota
media = soma_nota/n

for j in range(len(vetor_nota)):
    if vetor_nota[j] > media:
        acima_media += 1
    elif vetor_nota[j] < media:
        abaixo_media += 1
    else:
        igual_media +=1

print(f"{round(media)} foi a media da sala")
print(f"{acima_media} foram as notas acima da média, {abaixo_media} foram as notas abaixo da media e {igual_media} foram as notas iguais a media")


