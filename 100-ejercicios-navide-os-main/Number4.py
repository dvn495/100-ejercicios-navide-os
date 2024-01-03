#ESTRUCTURA REPETITIVA MAYOR PROMEDIO

xpro = 0
for i in range(1,6):
    nom = input("INGRESE EL NOMBRE: ")
    pro = float(input("PROMEDIO         : "))
    if (xpro < pro):
        xpro = pro
        xnom = nom

print(f"ESTUDIANTE CON MAYOR NOTA: {xnom}")
print(f"PROMEDIO                 : {xpro}")
