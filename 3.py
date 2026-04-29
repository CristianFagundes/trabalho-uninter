soma = 0 
while True:
    valor = int(input("informe um numero entre 1 a 100 (0 para sair)"))
    match valor:
        case valor if valor >= 1 and valor <= 100:
            soma += valor 
        case 0:
            print(f"valor total: {soma}")
            break
        case _:
            print("valor invalido")  