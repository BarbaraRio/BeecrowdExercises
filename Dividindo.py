quantidade = int(input())

for i in range(quantidade):
    valores = []
    entradas = input().split()
    
    for num in entradas:
        valores.append(int(num))
    A = valores[0]
    B = valores[1]

    if B == 0:
        print("divisao impossivel")
    else:
        print("%.1f"%(A/B))