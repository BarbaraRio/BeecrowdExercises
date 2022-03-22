entrada = input().split()
valores = []

#Convertendo em float
for num in entrada:
    valores.append(float(num))

#Verificando se é um triângulo
A = max(valores)
valores.remove(max(valores))
C = min(valores)
valores.remove(min(valores))
B = valores[0]

if A >= (B + C):
    area = ((A + B) * C) / 2
    print("Area = {}".format(area))
else:
    print("Perimetro = {}".format(A + B + C))