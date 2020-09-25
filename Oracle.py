from random import randint

seq_num = 12
num_jogadas = 3
round = 1

print ('#######################')
print ('Ask To Oracle, the game')
print ('#######################')

while (round <= num_jogadas):

  print ('Tentativa {} de {}'.format(round,num_jogadas))
  tentativa = int(input('Advinhe a sequencia numérica: '))
  num_maior = tentativa > seq_num
  num_menor = tentativa < seq_num

  if tentativa == seq_num:
      print ('você acertou!')
      break
  else:
    if num_maior:
      print('O número digitado está acima do número buscado!')
    elif num_menor:
      print('O número digitado está abaixo do número buscado!')
  round += 1
 
  print ('O número digitado foi: ', tentativa)
  print('----------------------------------------------------')
while tentativa != seq_num:
  print ('Game Over!')
  break