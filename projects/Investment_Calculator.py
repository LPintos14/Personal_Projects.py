"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión en años y en meses, y si te da en dias"""

def calculadora():#funciona
    cuenta=True
    while cuenta==True:
        try:
            inversion=float(input(f'¿Cuanto dinero queres invertir {nombre}?: '))
            tna=float(input(f'¿De cuanto es la tasa nominal anual?: '))
            años=int(input(f'¿Cuantos años vas a invertirlo?: '))
            ganancia=round((inversion*(tna/100)*años),2)
            capital_nuevo=ganancia+inversion
            tnm=(tna/100)/12
            ganancia_mensual=round((inversion*tnm),2)
            meses=años/12
            print(f'Bueno {nombre}, en {años} años, con la tasa porcentual anual de {tna}%, vas a generar una ganancia de ${ganancia}.\nLo que significa que tu capital inicial de ${inversion} va a pasar a ser de ${capital_nuevo} en {años} años.\nTambien te lo dejo en cantidades por mes.\nEs decir que por mes, tu inversion de ${inversion} por mes te dara como interes ${ganancia_mensual}, elevando tu capital incial a la suma de {inversion+ganancia_mensual} ')
            cuenta=False
            break
        except:
            print(f'Por favor {nombre}, usa solo numeros para esta parte. Vamos desde el principio')



print("Bienvenido a la calculadora de inversiones")
usar=True
while usar==True:
    uso=str(input("¿Queres usarme para calcular tus intereses?\nRespondeme por Si o por No\n")).title()
    if uso=="No":#funciona
        print("Esta bien\nUna lastima no poder ayudarte")
        print("Nos vemos la proxima")
        print("Adios")
        usar=False
    elif uso=="Si":
        print("Te voy a ayudar a calcular la cantidad de interes que podes generar\nTambien te voy a decir cuanto más capital vas a tener luego de tu inversion")
        print("Para comenzar, decime tu nombre por favor")
        nombre=input().title()#hasta aca funciona
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
                print("genial!!!")
                calculadora()
            else:
                print("")
                print(f'Por favor {nombre}, elegi por si o por no')
                print("")
    else:#funciona
        print("")
        print(f'Por favor, elegi por si o por no')
        print("")



