import random

lista1 = []
while 10 not in lista1:
    for x in range(100):
        n = random.randrange(11)
        lista1.append(n)
        if 10 in lista1:
            break
    print(lista1)
    print (len(lista1))
    