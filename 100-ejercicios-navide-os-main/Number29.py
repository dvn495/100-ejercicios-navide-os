#CANTIDAD DE PARES E IMPARES

sumaP = 0
sumaI = 0

num = int(input("INGRESE NUMERO: "))

for i in range (1,num+1):
    if ((i % 2)==0):
        sumaP += i
    else:
        sumaI += i

print (f"SUMA DE NUMEROS PARES  : {sumaP}")
print (f"SUMA DE NUMEROS IMPARES: {sumaI}")