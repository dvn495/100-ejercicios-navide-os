
h = int(input("HORAS:"))
m = int(input("MINUTOS: "))
s = int(input("SEGUNDOS: "))
costo = ((h*3600) + (m*60)+ s)*0.25
print(f"\nCOSTO TOTAL: {costo}")