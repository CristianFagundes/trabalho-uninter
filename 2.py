pessoas = []
for p in range(1,6):
    pessoa = {}
    pessoa['nome'] = input(f"iNFORME O NOME DA {p}ª pessoa: ")
    pessoa['sobrenome'] = input(f"Informe o sobrenome da {p}º pessoa: ")
    pessoa['idade'] = int(input(f"Informe a idade da {p}º pessoa: "))
    pessoa['salario'] = float(input(f"Informe o salario da {p}º pessoa: "))
    pessoas.append(pessoa)

for pessoa in pessoa:
    for chave, valor in pessoas.items():
        print(f"{chave}: {valor}")
    print()