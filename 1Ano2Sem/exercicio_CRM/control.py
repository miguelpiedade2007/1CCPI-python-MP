from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent/"data"
#DATA_DIR.mkdir(exist_ok=TRUE) cria o arquivo caso não tenha
print(DATA_DIR)
DB_PATH = DATA_DIR / "leads.json"

#CRUD
#Create / Read / Update / Delete

#READ

def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(enconding="utf-8"))
    except json.JSONDecodeError:
        return []

#CREATE
#desafio otimizar (similar a Big O), aqui para escrever/cadastrar ou ler um usuário todos os outros serão lidos ou escritos novamente
#pense em uma maneira de concertar isso
def create_lead(lead_dict):
    leads =read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=8), encoding="utf-8")


# Buscar Leads pela query
def read_leads_search(query):
    #função que busca por leads a partir da query e retorna uma lista com resultados
    leads = read_leads()
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]}".lower()
        print(txt_lead)

        if query.lower() in txt_lead:
            results.append((i, lead))


    return results

# Exportar leads para CSV
def export_csv():
    #Exporta todos os leads para csv e retorna o caminho do arquivo csv
    path_csv = DATA_DIR / "leads.csv"
    leads = read_leads()

    try:
        with path_csv.open("w", newline="")