total = int(input())
cont = 0
dentro = 0
out = 0

while cont < total:
  num = int(input())
  cont += 1
  if (num >= 10) and (num <= 20):
    dentro += 1
  else:
    out += 1
print("%d in"%(dentro))
print("%d out"%(out))