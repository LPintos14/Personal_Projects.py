def calculadora():
    cuenta=True
    while cuenta==True:
        try:
            inversion=float(input(f'¿Cuanto dinero queres invertir {nombre}?: '))
            tna=float(input(f'¿De cuanto es la tasa nominal anual?: '))
            tnm=(tna/100)/12
            tasa_diaria=(tna/100)/365
            meses=int(input(f'¿Cuanto tiempo vas a invertirlo? (expresalo en meses): '))
            ganancia=round((inversion*tnm)*meses,2)
            capital_nuevo=ganancia+inversion
            print(f'Bueno {nombre}, con la contratacion de tu plazo fijo, con un capital inicial de ${inversion}, considerando la tasa nominal anual de {tna}%, te puedo decir que en {meses} meses vas a generar un interes de ${ganancia}, haciendo que tu capital aumente a un total de ${capital_nuevo}')
            cuenta=False
            break
        except:
            print(f'Por favor {nombre}, usa solo numeros para esta parte. Vamos desde el principio')



print("Bienvenido a la calculadora de plazo fijo")
usar=True
while usar==True:
    uso=str(input("¿Queres usarme para calcular los intereses de tu plazo fijo?\nRespondeme por Si o por No\n")).title()
    if uso=="No":
        print("Esta bien\nUna lastima no poder ayudarte")
        print("Nos vemos la proxima")
        print("Adios")
        usar=False
    elif uso=="Si":
        print("Te voy a ayudar a calcular la cantidad de interes que va a generar tu plazo fijo\nTambien te voy a decir cuanto más capital vas a tener luego del plazo que dispongas")
        print("Para comenzar, decime tu nombre por favor")
        nombre=input().title()
        print(f'Hola {nombre}, bienvenide')
        calculadora()
        seguir=True    
        while seguir==True:
            try:
                opcion=str(input(f'{nombre}, ¿Queres volver a usarme?\n')).title()
            except:
                print(f'Por favor {nombre}, elegi por si o por no')
            if opcion=="No":
                print("Esta bien\nUn placer haberte ayudarte")
                print("Nos vemos la proxima")
                print("Adios")
                seguir=False
                usar=False
            elif opcion=="Si":
                print("!!!genial!!!")
                calculadora()
            else:
                print("")
                print(f'Por favor {nombre}, elegi por si o por no')
                print("")
    else:
        print("")
        print(f'Por favor, elegi por si o por no')
        print("")
