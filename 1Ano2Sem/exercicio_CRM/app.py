import repo
import control

from model import model_lead

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    status = input("Status: ")

    #Validação de dados ...
    #depois de validad precisamos modelar os dados
    #vamos modlar os leads como um dicionáio
    print(model_lead(name, email, status))

    #depois do meu lead modelado como dict, precisamos enviar o dict para o leads.json
    #vamos usar o control para isso

    print("Lead adicionado (func")

def main():
    while True:
        print("\n Mini CRM de leads")
        print("[1] Adicionar Lead")
        print("[2] Listar Lead")
        print("[0] Sair do programa")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            add_lead()
        elif opc == "2":
            print("Listar leads")
        elif opc == "0":
            print("Sair do programa")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()