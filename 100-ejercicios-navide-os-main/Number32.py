#REGALOS SEGUN EDAD Y SEXO

diax= 21
mesx = 10 
aniox = 2023
edad = 0

for i in range(1,11):
    dni = input("DNI: ")
    dia = int(input("DIA DE NACIMIENTO: "))
    mes = int(input("MES DE NACIMIENTO: "))
    anio = int(input("AÑO DE NACIMIENTO: "))
    genero = input("GENERO (H/M): ").upper()
    print  (f"FECHA ACTUAL {diax}/{mesx}/{aniox}")

    edad = aniox - anio
    if (mes > mesx):
        edad -= 1
    elif ( mes == mesx and dia > diax):
        edad -= 1
    
    if (edad >= 8):
        print ("RECIBE TABLET")
    elif( edad == 6):
        if(genero == "H"):
            print ("RECIBE CARRITO")
        elif (genero == "M"):
            print ("RECIBE MUÑECA")
