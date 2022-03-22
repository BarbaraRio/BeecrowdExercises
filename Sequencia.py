while True:
    val = []
    entrada = input().split()
    for num in entrada:
        val.append(int(num))
    A = val[0]
    B = val[1]
    if A == B:
        break
    else:
        if A > B:
            print("Decrescente")
        else:
            print("Crescente")
