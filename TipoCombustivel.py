cont_1 = 0
cont_2 = 0
cont_3 = 0

while True:
  n = int(input())
  if n < 1 or n > 4:
    n = int(input())
  if n == 4:
    break
  if n == 1:
    cont_1 += 1
  elif n == 2:
    cont_2 += 1
  elif n == 3:
    cont_3 += 1

print("MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d"%(cont_1, cont_2, cont_3))