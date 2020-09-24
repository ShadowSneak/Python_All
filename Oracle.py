from random import randint

seq_num = randint(0, 11)
sim = ('sim', 'Sim', 's', 'S')
nao = ('nao', 'Nao', 'n', 'N')
num_maior: tentativa > seq_num
num_menor: tentativa < seq_num

print ('################')
print ('Ask To Oracle, the game')
print ('################')

tentativa = int(input('Advinhe a sequencia numérica: '))
if tentativa == seq_num:
    print ('você acertou!')
else:
    pass

    

def tentativa_loop():
  tentativa = int(input('Advinhe a sequencia numérica: '))
print ('O número digitado foi: ', tentativa)
if tentativa == seq_num:
    print ('você acertou!')
else:
    if num_maior:
        print('O número digitado está acima do número buscado!')
    elif num_menor:
        print('O número digitado está abaixo do número buscado!')


while True:
  s_n = input('Deseja continuar? (sim/não): ')
  if s_n in sim:
    tentativa_loop()
    
  elif s_n in nao:
    break

  else:
    print ('é sim ou nao!')
