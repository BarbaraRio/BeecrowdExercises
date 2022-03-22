valores = input().split()
num = []

for i in valores:
    i = int(i)
    num.append(i)

A, B, C, D = num

if (B > C) and (D > A) and ((C + D) > (A + B)) and (C and D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
