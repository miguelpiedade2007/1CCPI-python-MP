import repo
from stages import model_lead





def main():
    while True:
        print("\ Mini CRM de leads")
        print("[1] Adicionar Lead")
        print("[2] Listar Lead")
        print("[0] Sair do programa")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            print("Lead adicionado")
        elif opc == "2":
            print("Listar leads")
        elif opc == "0":
            print("Sair do programa")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()