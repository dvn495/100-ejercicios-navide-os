#NUMEROS DEL Rango menor a mayor

a = int(input("NUMERO A: "))
b = int(input("NUMERO B: "))

if (a<b):
    for i in range(a+1,b):
        print (i)
else:
    i = b+1
    for i in range(b+1,a):
        print (i)