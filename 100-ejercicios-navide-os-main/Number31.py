#LETRAS CONSONANTES

c= 0
s= 0
d= 0
l= 0
r= 0
m =0
refran = " "
consonante = 0

ref = input("INGRESE REFRAN: ")

for i in range(len(ref)):
    if (ref[i] != " "):
        refran =  refran + ref[i]

for i in range(len(refran)):
    letra = (ref[i]).upper()
    if (letra == "C"):
        c += 1
    elif ( letra == "S"):
        s +=1
    elif ( letra == " D") :
        d += 1                                                                                  
    elif ( letra == "L"):
        l += 1
    elif ( letra == "R"):
        r += 1
    elif (letra == "M"):
        m += 1
    elif letra not in ["A","E","I","O","U"]:
        consonante += 1
    
print (f"CANTIDAD DE C: {c}")    
print (f"CANTIDAD DE S: {s}")
print (f"CANTIDAD DE D: {d}")
print (f"CANTIDAD DE L: {l}")
print (f"CANTIDAD DE R: {r}")
print (f"CANTIDAD DE M: {m}")
print (f"CANTIDAD DE CONSONANTES: {consonante}")