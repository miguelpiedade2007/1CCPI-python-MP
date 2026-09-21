import lead
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

#Desafio formatar a saída como tabela
def list_leads():
    leads = control.read_leads()
    print(leads)
    print(f"## | {"Nome":<15} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | lead{"nome":<15} | {lead["email"]}:")


def search_leads():
    query = input("Buscando por: ").strip().lower()


    #Control
    #comparação entre query digitada e o leads.json
    search_results = control.read_leads_search(query)


def export_leads():
    print("Lead exportado")

def main():
    while True:
        print("\n Mini CRM de leads")
        print("[1] Adicionar Lead")
        print("[2] Listar Lead")
        print("[3] Buscar (nome/email)")
        print("[4] Sair")
        print("[0] Sair do programa")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            add_lead()
        elif opc == "2":
            list_leads()
        elif opc == "0":
            print("Sair do programa")
            break
        elif opc == "3":
            search_leads()

        elif opc == "4":
            export_leads()

        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()