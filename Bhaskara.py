import math

valores = input().split()
num = []

for i in valores:
    i = float(i)
    num.append(i)

A, B, C = num

if A == 0 or B == 0 or C == 0:
    print("Impossivel calcular")
else:
    delta = ((B ** 2) - (4 * A * C))
    if delta < 0:
        print("Impossivel calcular")
    else:
        r1 = (-B + (math.sqrt(delta))) / (2 * A)
        r2 = (-B - (math.sqrt(delta))) / (2 * A)

        print("R1 = %.5f"%(r1))
        print("R2 = %.5f"%(r2))