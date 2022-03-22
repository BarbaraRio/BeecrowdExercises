cont = 0
soma = 0

while cont < 2:
    while True:
        nota = float(input())
        if (nota < 0) or (nota > 10):
            print("nota invalida")
        else:
            break
    cont += 1
    soma += nota


media = soma / 2
print("media = %.2f"%(media))