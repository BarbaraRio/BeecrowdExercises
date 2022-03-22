salario = float(input())

if 400.00 >= salario:
    percentual = '15 %'
    reajuste = salario * 0.15
    novo_salario = salario + reajuste

elif salario >= 400.1 and salario <= 800.00 :
    percentual = '12 %'
    reajuste = salario * 0.12
    novo_salario = salario + reajuste

elif salario >= 800.01 and salario <= 1200.00:
    percentual = '10 %'
    reajuste = salario *0.10
    novo_salario = salario + reajuste

elif salario >= 1200.01 and salario <= 2000.00:
    percentual = '7 %'
    reajuste = salario * 0.07
    novo_salario = salario + reajuste

elif salario > 2000.00:
    percentual = '4 %'
    reajuste = salario * 0.04
    novo_salario = salario + reajuste

print("Novo salario : %.2f\nReajuste ganho: %.2f\nEm percentual: %s"%(novo_salario, reajuste, percentual))
