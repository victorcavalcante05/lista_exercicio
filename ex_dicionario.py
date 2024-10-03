nota_final = float(input("Informe a nota obtida: "))

if nota_final < 6.0:
    print("Resultado: Reprovado")
elif 6.0 <= nota_final < 7.0:
    print("Resultado: Recuperação")
elif 7.0 <= nota_final < 8.0:
    print("Resultado: Aprovado")
elif 8.0 <= nota_final < 9.0:
    print("Resultado: Aprovado")
elif 9.0 <= nota_final <= 10.0:
    print("Resultado: Aprovado com Distinção")
else:
    print("Nota inválida, por favor verifique o valor inserido.")

input_cor = input("Informe uma cor: ").lower()

cores_primarias = ["vermelho", "azul", "amarelo"]
cores_secundarias = ["verde", "laranja", "roxo"]

if input_cor in cores_primarias:
    print("A cor é Primária")
elif input_cor in cores_secundarias:
    print("A cor é Secundária")
else:
    print("A cor pertence a outro grupo")

numero_mes = input("Insira o número do mês (01 a 12): ")
meses_ano = {
    "01": "Janeiro",
    "02": "Fevereiro",
    "03": "Março",
    "04": "Abril",
    "05": "Maio",
    "06": "Junho",
    "07": "Julho",
    "08": "Agosto",
    "09": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro"
}

print(f"O mês é: {meses_ano.get(numero_mes, 'Mês inválido')}")

mes_nome = "Fevereiro"
ano_atual = 2024

def verifica_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

meses_31_dias = [meses_ano["01"], meses_ano["03"], meses_ano["05"], meses_ano["07"], meses_ano["08"], meses_ano["10"], meses_ano["12"]]
meses_30_dias = [meses_ano["04"], meses_ano["06"], meses_ano["09"], meses_ano["11"]]

if mes_nome in meses_31_dias:
    print(f"{mes_nome} tem 31 dias.")
elif mes_nome in meses_30_dias:
    print(f"{mes_nome} tem 30 dias.")
else:
    if verifica_bissexto(ano_atual):
        print(f"{mes_nome} tem 29 dias por ser ano bissexto.")
    else:
        print(f"{mes_nome} tem 28 dias.")
