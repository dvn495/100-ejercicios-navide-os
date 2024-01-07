#ALGORITMO QUE MUESTRA LA CANTIDAD DE VOCALES
import os
a = 0
e = 0
i = 0
o = 0
u = 0
frase = input("FRASE: ").upper()
for vocal in frase:
    if (vocal == "A" or vocal == "Á"):
        a +=1
    if (vocal == "E" or vocal == "É"):
        e +=1
    if (vocal == "I" or vocal == "Í"):
        i += 1
    if (vocal == "O" or vocal == "Ó"):
        o += 1
    if (vocal == "U" or vocal == "Ú"):
        u += 1

print(f"Cantidad de vocales\n A: {a}\n E: {e}\n I: {i}\n O: {o}\n u: {u}")
os.system("pause")