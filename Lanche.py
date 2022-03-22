valores = input().split()
num = []
cont = 0

for i in valores:
    valores = int(i)
    num.append(valores)
    cont += 1
    if cont == 2:
        break

if num[0] == 1:
    print("Total: R$ %.2f"%(num[1] * 4))
elif num[0] == 2:
    print("Total: R$ %.2f"%(num[1] * 4.5))
elif num[0] == 3:
    print("Total: R$ %.2f"%(num[1] * 5))
elif num[0] == 4:
    print("Total: R$ %.2f"%(num[1] * 2))
elif num[0] == 5:
    print("Total: R$ %.2f"%(num[1] * 1.5))