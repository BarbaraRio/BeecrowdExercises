entrada = input().split()
valores = []

#Convertendo em float
for num in entrada:
    num = float(num)
    valores.append(num)

#Estabelecendo A, B e C
A = max(valores)
valores.remove(max(valores))
C = min(valores)
valores.remove(min(valores))
B = valores[0]

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if A ** 2 == (B ** 2 + C ** 2):
        print("TRIANGULO RETANGULO")
    if A ** 2 > (B ** 2 + C ** 2):
        print("TRIANGULO OBTUSANGULO")
    if A ** 2 < (B ** 2 + C ** 2):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if A == B and (A != C or B != C):
        print("TRIANGULO ISOSCELES")
    if B == C and (B != A or C != A ):
        print("TRIANGULO ISOSCELES")