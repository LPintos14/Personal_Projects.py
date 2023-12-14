def Regla_directa(num1,num2,x):
   
    y=((num2*x)/num1)
    valor=round(y,2)
    print(f'El valor de tu incognita es de {valor}')
def Regla_inversa(num1,num2,x):
    
    y=((num1*x)/num2)
    valor=round(y,2)
    print(f'El valor de tu incognita es de {valor}')
def Directa():
    regla=True
    while regla==True:
        try:
            num1=float(input("Ingresa tu primer valor: "))
            x=float(input(f'Ingresa el valor relacionado con {num1}: '))
            num2=float(input("Ingresa tu segundo valor: "))
        except:
            print(f'Por favor {nombre}, ingresa valores numericos. Volvamos a empezar')   
        else:
            Regla_directa(num1,num2,x)
            break
def Inversa():
    regla=True
    while regla==True:
        try:
            num1=float(input("Ingresa tu primer valor: "))
            x=float(input(f'Ingresa el valor relacionado con {num1}: '))
            num2=float(input("Ingresa tu segundo valor: "))
        except:
            print(f'Por favor {nombre}, ingresa valores numericos. Volvamos a empezar')   
        else:
            Regla_inversa(num1,num2,x)
            break
def Seguir_jugando():
    uso=True
    print("Genial!!!")
    while uso==True:
        opcion=str(input(f'¿Que tipo de relacion te gustaria?\nDirecta\nInversa\nTu eleccion: ')).title
        if opcion=="Directa":
            Directa()
            break
        elif opcion=="Inversa":
            Inversa()
            break
        else:
            print("")
            print(f'Por favor {nombre}, elegi una de las opciones dadas')
            print("")

print("Buenas Buenas")
print("Vamos a usar la Calculadora de Regla de 3 Simple")
nombre=input("Ingresa tu nombre para comenzar o escribe salir para abandonar la calculadora.\n").title()
if nombre=="Salir":
    print("")
    print("Una lastima verte partir")
    print("Adios")
else:
    calculadora=True
    while calculadora==True:
        usar=str(input(f'Hola {nombre}, que te gustaria hacer\nUsar calculadora\nSalir\nTu eleccion: ')).title()
        if usar=="Salir":
            print(f'Genial {nombre}, nos vemos la proxima')
            print("Adios")
            calculadora=False
        elif usar=="Usar Calculadora":
            uso=True
            print("Genial!!!")
            while uso==True:
                opcion=str(input(f'¿Que tipo de relacion te gustaria?\nDirecta\nInversa\nTu eleccion: ')).title()
                if opcion=="Directa":
                    Directa()
                    seguir=True
                    break
                elif opcion=="Inversa":
                    Inversa()
                    seguir=True
                    break
                else:
                    print("")
                    print(f'Por favor {nombre}, elegi una de las opciones dadas')
                    print("")
            while seguir==True:
                sigo=str(input(f'¿{nombre}, queres volver a usar la calculadora?\nSi\nNo\nTu eleccion: ')).title()
                if sigo =="No":
                    print(f'Genial {nombre}, nos vemos la proxima')
                    print("Adios")
                    seguir=False
                    calculadora=False
                    break
                elif sigo=="Si":
                    Seguir_jugando()
                else:
                    print("")
                    print(f'Por favor {nombre}, elegi una de las opciones dadas')
                    print("")
        else: 
            print("")
            print(f'Por favor {nombre}, elegi una de las opciones dadas')
            print("")
        