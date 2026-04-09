from IPython.core.inputtransformer2 import TokenTransformBase
#Pizzaria do Cristian,Pedro ERmiro e Gustavo
print("                        Bem-vindo a Pizzaria do Cristian                                ")
print("                              Cardapio                                                  ")
print("                                                                                        ")
print("     | Tamanho    |  Pizza Salgadas(PS)     |  Pizza Doce(PD)                           ")
print("     |    P       |     R$  30.00           |    R$  34.00                              ")
print("     |    M       |     R$  45.OO           |    R$  48.00                              ")
print("     |    G       |     R$  60.00           |    R$  66.00                              ")
print("                                                                                        ")
print("     |   Refrigerante 2L    R$ 15.00   |       ")
print("     |  NAO REALIZAMOS ENTREGAS PARA DISTANCIA ACIMA DE 25KM  | ")

#limite 5 pizza e 2 Refrigerante !!!
total=0
while True:
  item = input("Entre com o intem que deseja (Pizza/Refrigerante) : ")
  if item != 'Pizza' and item != 'Refrigerante':
    print("item invalido!")

  elif item == "Refrigerante" :
    print("Refrigerante de 15.00")
    total=total+15
    break

while True:
  opcao = input("Deseja mais alguma coisa? (s/n)")
if opcao == "s"














