ponto1 = input().split()
ponto2 = input().split()
lista_1 = []
lista_2 = []

#Convertendo 
for val_1 in ponto1:
    val_1 = float(val_1)
    lista_1.append(val_1)
for val_2 in ponto2:
    val_2 = float(val_2)
    lista_2.append(val_2)

#Fórmula
x = ((lista_2[0] - lista_1[0]) ** 2)
y = ((lista_2[1] - lista_1[1]) ** 2)

distancia = (x+y) ** 0.5
print("%.4f"%(distancia))