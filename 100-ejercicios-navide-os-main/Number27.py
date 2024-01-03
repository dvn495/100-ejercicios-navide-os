#SERIE DE NUMEROS PRIMOS
divisible = 0
num = int(input("INGRESE UN VALOR: "))
for i in range(2, num+1):
    for item in range (1,i+1):
        if ((i % item)== 0):
            divisible +=1
    if (divisible == 2):
        print (f"{i} ")
    divisible = 0
print (" ")