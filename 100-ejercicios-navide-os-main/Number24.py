#MOSTRAR EL FACTORIAL DE UN NUMERO

fact = 1
num = int(input("FACTORIAL A CALCULAR: "))
print (" ")
print ("SERIE DE FACTORIAL: ")

for i in range(1,num+1):
    print(f"{(num + 1) - i}  ")
    fact = fact * i

print (" ")
print (f"EL FACTORIAL ES: {fact}")
