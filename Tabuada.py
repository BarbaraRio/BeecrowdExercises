num = int(input())
cont = 0

while cont <= num:
  if cont > 10:
    break
  else:
    resultado = num * cont
    cont += 1
  print("%d x %d = %d"%(cont, num, resultado))