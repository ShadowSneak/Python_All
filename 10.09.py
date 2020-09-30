'''
lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b', 'c', 'd']

for x in lista1:
    lista2.append(x)
    print (x)
'''
'''
lista1 = []
lista2 = ['dia', 'mes', 'ano']
for x in range(9):
    for h in lista2:
        print (h, x)
    lista1.append(x)

else:
    print ('It has', x, 'numbers')
    print (lista1)
'''

tupla = (1, 2, 3, 4, 5)

lista = list(tupla)

lista[0] = 0

tupla1 = tuple(lista)

print (tupla1)
print (tupla1[2])
print (len(tupla))

'''
aster = 0
for y in range(11):
   while aster <= y:
    aster += 1
    
    print (y)
    print (aster)
'''
