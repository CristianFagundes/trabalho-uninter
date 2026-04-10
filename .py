

soma = 0 
valores = [] 
#codigo principal
while True:
    valor = float(input("informe m numero: "))
    
    if valor == 0:
        break
    elif valor < 0:
        print("informe um numero positivo!")
        continue
    else:
        soma += valor

print(f"a soma dod valores é: {soma}")
print(f"os valores somados foram:\n{valor}")

    
