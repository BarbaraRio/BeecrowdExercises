num = int(input())

horas = num//3600
num %= 3600
minutos = num // 60
num %= 60
segundos = num

print("%d:%d:%d"%(horas, minutos, segundos))