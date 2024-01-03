#DESCUENTO MAYOR DE $50

total=0
desc=0

for i in range(1,11):
    consumo = int(input(f"Consumo {i}: $"))
    total += consumo

if (total > 50 ):
    desc = total * 0.07

print (f"CONSUMO TOTAL: ${total}")
print (f"DESCUENTO:     ${desc}")
print (f"PAGO TOTAL:    ${total-desc}")