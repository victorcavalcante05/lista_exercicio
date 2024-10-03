# 1.	Escreva um programa que percorra uma lista de notas e classifique cada uma das seguintes maneiras:
# "Reprovado" (nota < 6,0)
# "Recuperação" (nota >= 6,0 e nota < 7,0)
# "Aprovado" (nota >= 70, e nota < 9,0)
# "Aprovado com Menção Honrosa" (nota >= 9,0)

nota = float(input("Digite a Nota:"))

if nota < 6:
    print("Reprovado")
elif nota >= 6 and nota < 7:
    print("Recuperacao")
elif nota >= 7 and nota < 8:
    print("Aprovado")
elif nota >=8 and nota < 9:
    print("Aprovado")
elif nota >=9 and nota <=10:
    print("Aprovado com Menção Honrosa")
else:
    print("Nota Digitada errada")

# 2.	Escreva um programa que percorra uma lista de cores e classifique-as como "Primárias" (vermelho, azul, amarelo)
    #  ou "Secundárias" (verde, laranja, roxo), ou "Outras".
cor = input("Digite a cor:")

# if cor =="vermelho" or cor=="azul" or cor=="amarelo":
#     print("Primaria")
# elif cor =="verde" or cor=="laranja" or cor=="roxo":
#     print("Secundaria")
# else:
#     print("Outras")

lista_primaria = ["vermelho", "azul", "amarelo"]
lista_secundaria = ["verde", "laranja", "roxo"]

if cor in lista_primaria:
    print("Primaria")
elif cor in lista_secundaria:
    print("Primaria")
else:
    print("Outras")

#Exercicio 3
mes = input("Digite o mes:")
dicionario = {"01": "Janeiro",
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
              "12": "Dezembro"}

print(dicionario[mes])

# Escreva um programa que verifique se o mês e ano 
# digitado pelo usuário tem 28,29,30 ou 31 dias.

#Entrada
mes = "Fevereiro"
ano = 2024
# Funcao Auxiliar para verificar se no ano é bisexto
def is_leap_year(year):
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return is_leap

lista_mes_31 = [ 
    dicionario["01"],
    dicionario["03"],
    dicionario["05"],
    dicionario["07"],
    dicionario["08"],
    dicionario["10"],
    dicionario["12"],
]
lista_mes_30 = [ 
    dicionario["04"],
    dicionario["06"],
    dicionario["09"],
    dicionario["11"],
]
if mes in lista_mes_31:
    print("Mes com 31 dias")
elif mes in lista_mes_30:
    print("Mes com 30 dias")
else:
    if is_leap_year(ano):
        print("Mes tem 29 dias")
    else:
        print("Mes tem 28 dias")


