
num = int(input("INGRESE UN NUMERO DE 3 CIFRAS: "))
cen = num-(num % 100)/100
res = num % 100
dec = (res-(res % 10))/10
uni = res % 10
print(f"\nCENTENA: {cen}\nDECENA: {dec}\n UNIDAD: {uni}")