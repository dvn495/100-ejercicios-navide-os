#PROMEDIO DE VARIAS NOTAS
suma = 0
n = int(input("INGRESE LA CANTIDAD DE NOTAS: "))
for i in range(1,n+1):
    nota = int(input(f"NOTA {i} : "))
    suma += nota

print (f"PROMEDIO: {suma/n}")