#TRIANGULO DE NUMEROS
n = 0
val = 1
cont = 1

print("MUESTRA GRAFICA DE NUMEROS COMO TRIANGULOS")

while n < 3:
    n = int(input("INGRESE NUMERO: "))

for i in range(0, n+1):
    espa = " "
    for z in range(1, n - i + 1):
        espa = espa + " "

    print(espa, end=" ")
    
    cont = 1
    for f in range(1, val + 1):
        print(cont, end=" ")
        if cont == 9:
            cont = 0
        else:
            cont += 1

    print()  
    val += 2



