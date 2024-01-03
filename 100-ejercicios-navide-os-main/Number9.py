#GRAFICA CONCATENAR

xn = 7
for i in range (1,8):
    serie = " "
    if (i >= 5):
        xn += 2

    for item in range ( xn - i):
        serie = serie + "*"
        
    print (serie)