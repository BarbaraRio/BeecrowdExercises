maior = 0
posicao = 0
for valor in range(100):
    num = int(input())
    if num > maior:
        maior = num
        posicao = valor + 1

print(maior)
print(posicao)