
xseg = int(input("CANTIDAD DE SEGUNDOS: "))
hor = (xseg /60)
min= (xseg -(hor*3600)/60)
seg = (xseg-((hor*3600)+(min*60)))
print(f"HORAS : {hor}\nMINUTOS : {min}\SEGUNDOS : {seg}")
