estado = int(input("Digite o código do seu Estado:"))
peso = float(input("qual peso da carga? "))
cc = int(input("qual código da carga? "))
#cc é código da carga
peso_toneladas = peso * 1000
if 20 <= cc:
    valor_carga = peso * 100
    imposto_carga = peso * 100
elif 21 < cc <= 30:
    valor_carga = peso * 250
    imposto_carga = peso * 250
elif 31 < cc <=40:
    valor_carga = peso *340
    imposto_carga = peso * 340

if estado == 1:
    imposto_individual = 0.35 * valor_carga
    imposto = valor_carga + 0.35 * valor_carga

elif estado == 2:
    imposto_individual = 0.25 * valor_carga
    imposto = valor_carga + 0.25 * valor_carga

elif estado == 3:
    imposto_individual = 0.15 * valor_carga
    imposto = valor_carga + 0.15 * valor_carga

elif estado == 4:
    imposto_individual = 0.05 * valor_carga
    imposto = valor_carga + 0.05 * valor_carga

elif estado == 5:
    imposto_individual = "0%"
    imposto = valor_carga





print(f"o peso em toneladas é {peso_toneladas}")
print(f"o preço da carga do caminhão é {valor_carga}")
print(f"você paga {imposto_individual} em impostos do Estado e {imposto_carga} pelo peso da carga")
print(f"o valor total é {valor_carga}")














