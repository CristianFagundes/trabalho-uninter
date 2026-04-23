nomes = ["Cristiano", "Maria", "João", "Ana", "Pedro", "Carla", "Rosa", "Paulo", "Sofia", "Lucas"]
nome_o = []

for nome in nomes:
    if  nome.lower()[-1] == "o":
        nome_o.append(nome)

nome_o.sort(reverse=True)
print(nome_o)