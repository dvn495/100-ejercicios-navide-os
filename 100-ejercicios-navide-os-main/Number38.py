#COLOR MAS VOTADO
r = 0
v = 0
a = 0

n = int(input("INGRESE LA CANTIDAD DE PERSONAS: "))
for i in range(1, n+1):
    c = " "
    print(f"PERSONA Nro {i}")
    while c not in ["ROJO", "VERDE", "AZUL"]:
        c= input("[ROJO - VERDE - AZUL] : ").upper()
    
    if c == "ROJO":
        r += 1
    elif c == "VERDE":
        v += 1
    elif c == "AZUL":
        a += 1

if (r > v and r > a):
    Mcolor = "ROJO"
elif (v > r and v > a):
    Mcolor = "VERDE"
else:
    Mcolor = "AZUL"

print(f"CANTIDAD DE COLOR ROJO: {r}\nCANTIDAD DE COLOR VERDE: {v}\nCANTIDAD DE COLOR AZUL: {a}\nEL COLOR MAS ELEGIDO FUE: {Mcolor}")

        

              