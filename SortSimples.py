valores = input().split()
lista = []
ordem = []

for num in valores:
    num = int(num)
    lista.append(num)
    ordem.append(num)

#Crescente
print(min(lista))
lista.remove(min(lista))
print(min(lista))
lista.remove(min(lista))
print(lista[0])
print('')

#Ordem
for i in ordem:
    print(i)