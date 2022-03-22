valores = input().split()


for i in range(len(valores)):
  valores[i] = float(valores[i])

#Triângulo 
trgl = (valores[0]*valores[2]/2)
#Círculo
crcl = ((valores[2]**2)*3.14159)
#Trapézio 
trpz = ((valores[0]+valores[1])*valores[2]/2)
#Quadrado
qudr = (valores[1]**2)
#Retângulo
rtgl = (valores[0]*valores[1])


print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f"%(trgl, crcl, trpz,qudr,rtgl))