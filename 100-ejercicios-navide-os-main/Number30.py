#VENTAS REALIZADAS

tvh = 0
tvm= 0
muj = 0

empleados =int(input("CANTIDAD DE EMPLEADOS: "))
print (" ")

for i in range(1,empleados+1):
    print (f"EMPLEADO Nro {i}/{empleados}")
    nom = input("NOMBRE: ")
    genero = input("GENERO (M/F)").upper()
    ventas = int(input("VENTAS: "))

    if (genero == "M"):
        tvh += ventas
    elif(genero == "F"):
        tvm += ventas
        muj += 1

print (F"TOTAL DE VENTAS EN HOMBRES: {tvh}")
print (f"TOTAL DE VENTAS EN MUJERES: {tvm}")
print(" ")
print(f"PORCENTADE DE MUJERES: {(muj*100)/empleados}%")
