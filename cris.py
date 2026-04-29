dados = [6,7,5,1,2]
for i in range(len(dados)-1):
    for j in range(len(dados)-1):
        if dados[j] > dados[j+1]:
            dados[j], dados[j+1] = dados[j+1], dados[j]
print(dados)