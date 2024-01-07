#TRIANGULO PASCAL


M = [[0 for _ in range(20)] for _ in range(20)]


print("MOSTRAR EL TRIÁNGULO DE PASCAL")
N = int(input("INGRESE DIMENSIÓN [MENOS O IGUAL A 20]: "))


for IZQ in range(1, N+1):
    for DER in range(1, N+1):
        M[IZQ-1][DER-1] = 0
for IZQ in range(1, N+1):
    M[IZQ-1][0] = 1
for DER in range(1, N+1):
    M[DER-1][DER-1] = 1
for fila in M:
    print(fila)

for IZQ in range(1, N+1):
    ESPACIOS = " "
    
 
    for E in range(1, N-IZQ+1):
        ESPACIOS += " "
    
    print(ESPACIOS, end="")

    for DER in range(1, IZQ+1):
        VAL = M[IZQ-1][DER-1]

        if VAL != 0:
            print(VAL, end=" ")
        else:
            pass

    print("")  


