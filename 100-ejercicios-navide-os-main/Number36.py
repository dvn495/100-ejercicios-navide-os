#SUMATORIA DE LA SERIE
sumatoria = 0
v = 4
v1 = 5  
v2 = 1
x = 2
x1 = 0.5
ope = "-"

print ("MUESTRA LA SERIE DE NUMEROS\n")
n = int(input("VALOR DE N: "))

for i in range(1, n+1):
    if ( i != n):
        print(f"{v}/{x} {ope} ",end=" ")
    else:
        print(f"{v}/{x} {ope}...",end=" ")

    if(i % 2 == 1):
        ope = "+"
        sumatoria += (v/x)
    else:
        ope = "-"
        sumatoria -= (v/x)

    v += v1
    v1  += v2
    v2 += 1
    x = x * x1
    x1 += x1


print(f"\nSUMATORIA: {sumatoria}")
