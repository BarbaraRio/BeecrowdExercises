idade = int(input())

anos = idade / 365 
meses = (idade % 365) / 30
dias = (idade % 365) % 30

print("%d ano(s)\n%d mes(es)\n%d dia(s)"%(anos, meses, dias))