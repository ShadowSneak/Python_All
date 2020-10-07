tupla = ()
lista = list(tupla)

nPira = int(input("Quantos '*' quer que sua pirâmide tenha?: "))

for x in range(nPira):
  lista.append("*")
  print (lista)