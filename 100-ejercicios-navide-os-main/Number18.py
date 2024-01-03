#NUMERO CAPICUA

tem = ""
num = (input("INGRESE NUMERO: "))
for i in range(len(num) - 1, -1, -1):
    subcadena = num[i:i+1]
    tem = tem + subcadena

print ("")
print (f"NUMERO INGRESADO: {num}")
print (f"NUMERO CAMBIADO : {tem}")

if (num == tem):
    print ("ES UN NUMERO CAPICUA")
else:
    print ("NO ES UN NUMERO CAPICUA ")