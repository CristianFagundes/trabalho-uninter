soma = 0
valores=float(input("digite um numero de 1 a 100(com ou sem casa decimais)"))
maior = valores
menor = valores
while valores !=0:
    
    if valores < 0:
        print("voce deve digita outro número: ")
    elif valores >=1 and valores <= 100:
        soma = soma + valores
        if valores > maior:
            maior = valores
        if valores < menor:
            menor = valores
    else:
        print("úmero inválido.digite um número de 1 a 100.")

    valores=float(input("digite um número de 1 a 100 (com ou sem casa decimais): "))

print(f"valor somado de todos os números digitados:{soma}")
print(f"menor valor digitado: {menor}")
print(f"maior valor digitado: {maior}")


 