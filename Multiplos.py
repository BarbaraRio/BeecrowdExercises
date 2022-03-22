entrada = input().split()
valores = []

#Convertendo em int
for num in entrada:
    valores.append(int(num))

#Estabelecendo a ordem
maior = max(valores)
menor = min(valores)

#Verificando se são múltiplos
if (maior % menor == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")