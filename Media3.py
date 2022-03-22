n = input().split()
notas = []

for i in n:
 n = float(i)
 notas.append(n)

nota_1 = notas[0] * 2
nota_2 = notas[1] * 3
nota_3 = notas[2] * 4
nota_4 = notas[3] * 1

media = (nota_1 + nota_2 + nota_3 + nota_4) / 10
print("Media: %.1f"%(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif  media >= 5.0 and media < 6.9:
    print("Aluno em exame.")
    nota = float(input())
    print("Nota do exame: %.1f"%(nota))
    nova_nota = (media + nota) / 2
    if nova_nota >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f"%(nova_nota))
    else: 
        print("Aluno reprovado.")
        print("Media final: %.1f"%(nova_nota))
else:
    print("Aluno reprovado.")