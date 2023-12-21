#PAR E IMPAR PARA

par = 0
impar = 0

for i in range(1,11):
    numero = int(input(f"Numero {i}: "))
    
    if numero % 2 == 0:
        par +=1
    else:
        impar +=1

print (f"cantidad de pares: {par}")
print (f"cantidad de impares: {impar}")