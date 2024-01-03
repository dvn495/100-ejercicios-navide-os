#MUESTRA TODO LOS NUMEROS CAPICUA DE 3 CIFRAS
c = 0
r = 0
c1 = 0
r1 = 0

for i in range (100, 1000):
    c = (i - (i%100))/100
    r =  i % 100
    c1 = (r -(r%10))/10
    r1 = r % 10
    if (i==((r1 *100)+ (c1 *10)+c)):
        print (f"{i} ")
print (" ")
