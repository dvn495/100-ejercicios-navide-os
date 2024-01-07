#GANANCIAS E UNA GARITA DE CONTROL
import os
bus = 0
van = 0
micro = 0
man = 0
noct = 0
header = """
GANANCIAS DE UNA GARITA DE CONTROL
----------------------------------
"""
cantidad = int(input(f"{header}\n CANTIDAD DE VEHICULOS\n"))

for i in range(1, cantidad+1):
    print(f"TIPO DE VEHICULO Nro {i}/{cantidad}")
    tipo = input(" 1. Omnibus\n 2. Minivan\n 3.Micro\n OPCION: ")
    if tipo == "1":
        tarifa = 13
        bus += tarifa
    elif tipo == "2":
        tarifa = 10
        van += tarifa
    elif tipo == 3:
        tarifa = 8
        micro += tarifa
    
    turno = input("\nTURNO M/N: ").upper()
    if turno == "M":
        man += tarifa
    elif turno == "N":
        noct += tarifa 

print (f"\nIMPORTE TURNO MAÑANA {man}\n IMPORTE TURNO NOCHE {noct}")
print (f"\nIMPORTE OMNIBUS :{bus}\nIMPORTE MINIVAN :{van}\nIMPORTE MICRO  :{micro}")