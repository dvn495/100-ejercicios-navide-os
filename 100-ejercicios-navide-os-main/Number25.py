#SERIE 1+ 2/3...

n = int(input("VALOR DE N: "))
suma = 1
d = 3
if (n > 1):
    print (f"{suma} +")
    for i in range (2, n+1):
        if (i == n):
            print ( f" {i} / {d}")
        else:
            print (f"{i} / {d} + ") 
        suma = suma + (i/d)
        d += 2

print(" ")
print(f"LA SUMA ES {suma}")
         
         