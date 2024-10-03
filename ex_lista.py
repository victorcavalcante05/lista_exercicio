# 23.	Crie uma nova lista nomes_maiusculos contendo os nomes da lista nomes em letras maiúsculas. Utilize um loop for para isso.
lista_nomes = ["Ana", "Pedro", "Maria", "João"]
nomes_maiusculos = []
for n in lista_nomes:
    nome = n.upper()
    nomes_maiusculos += [nome]
    print(n)
print(nomes_maiusculos)
