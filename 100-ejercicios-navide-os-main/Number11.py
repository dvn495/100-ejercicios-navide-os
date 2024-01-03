#CALCULAR EL PRODUTO DE N NUMEROS

pro = 1
n = int(input ("EL VALOR DE N ES: "))
for i in range (1,n+1):
    print (f"{i} ")
    pro = (pro * i)

print ("")
print (f"PRODUCTO DE {n} ES: {pro}")