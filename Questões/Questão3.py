from datetime import datetime, date


def calcular_juros(valor, data_vencimento):
    hoje = date.today()

    dias_atraso = (hoje - data_vencimento).days

    if dias_atraso <= 0:
        return 0, 0, valor

    taxa_diaria = 0.025

    juros = valor * taxa_diaria * dias_atraso

    valor_final = valor + juros

    return dias_atraso, juros, valor_final


valor = float(input("Digite o valor da dívida: "))

data_texto = input(
    "Digite a data de vencimento (dd/mm/aaaa): "
)

try:
    data_vencimento = datetime.strptime(
        data_texto,
        "%d/%m/%Y"
    ).date()

except ValueError:
    print("Data inválida. Use o formato dd/mm/aaaa.")
    exit()


dias_atraso, juros, valor_final = calcular_juros(
    valor,
    data_vencimento
)


print("\n===== RESULTADO =====")
print(f"Valor original: R$ {valor:.2f}")
print(
    f"Data de vencimento: "
    f"{data_vencimento.strftime('%d/%m/%Y')}"
)
print(f"Dias de atraso: {dias_atraso}")
print(f"Juros: R$ {juros:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")