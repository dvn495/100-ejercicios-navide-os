#MOSTRAR SI UN NUMERO ES PRIMO  
divisi = 0
num = int(input("INGRESE NUMERO "))
for i in range(1,num+1):
    if ((num % i)== 0):
        divisi += 1

if (divisi == 2):
    print ("NUMERO PRIMO")
else:
    print ("NO ES PRIMO")