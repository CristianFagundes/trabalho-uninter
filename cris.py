nomes = ["JESSICA", "GESSICA","VANESSA","SUSANA","MARIANA",]
nome_2S = []

for nome in nomes:
    if  nome.lower().count("s") == 2:
        nome_2S.append(nome)

print(nome_2S)
    