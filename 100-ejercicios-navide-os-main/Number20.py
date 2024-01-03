#ENCONTRAR UN NUMERO ALEATORIO DEL 1 AL 20
import random
sw = 0
numA = random.randint(1,20)

for i in range (1,4):
    num = int(input("ENCUENTRE EL NUMERO[1-20] "))
    if ( num == numA):
        print("NUMERO ENCONTRADO")
        sw = 1
        i = 3
    else:
        if (num > numA):
            print ("INGRESE UN NUMERO MENOR")
        else:
            print ("INGRESE UN NUMERO MAYOR")

if (sw == 0 ):
    print (f"EL NUMERO A ENCONTRAR ERA: {numA}")