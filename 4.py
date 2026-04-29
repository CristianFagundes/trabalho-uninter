dados = ["Bruno", 42, 3.14, 3, "C", []]
for d in dados:
  match d:
   case str(d):
    print("Sring: ", d)
   case int(d):
    print("Inteiros: ",d)
   case float(d):
    print("float: ", d)
   case _:
    print("caso default, tipo desconhecido")

            