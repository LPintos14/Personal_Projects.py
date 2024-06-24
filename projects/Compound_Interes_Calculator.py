def interes_compuesto():
    interes=(capital_inicial)*(1+(tasa_anual/100)/n)**(t*n)
    return interes

print("Esta es la claculadora de interes compuesto")
print("Primero vamos a presentarnos")
nombre=input("¿Cual es tu nombre?: ").title()

print(f'Hola {nombre}, yo soy la calculadora')
print("Yo voy a ayudarte a calcular los interes compuestos de tu inversion")
print("Para eso vamos a necesitar\nAlgunos datos")
uso=True
calculadora=True
while uso==True:
    while calculadora==True:
        try:
            capital_inicial=float(input("Ingresa tu inversion incial: "))
            tasa_anual=int(input("Ingresa la Tasa Nominal Anual: "))
            tiempo=True
            while tiempo==True:
                try:
                    n=str(input("Ingresa el plazo de capitalizacion de los interes.\n1.Anual\n2.Semestral\n3.Trimestral\n4.Mensual\n")).title()
                except:
                    print(f'Por favor {nombre}, elegi un de las opciones validas')
                if n=="Anual":
                    n=1
                    plazo="Anual"
                    break
                elif n=="Semestral":
                    n=2
                    plazo="Semestral"
                    break
                elif n=="Trimestral":
                    n=4
                    plazo="Trimestral"
                    break
                elif n=="Mensual":
                    n=12
                    plazo="Mensual"
                    break
                else:
                    print(f'por favor {nombre}, elegi un de las opciones validas')
            t=float(input("Ingresa la cantidad de años que va a estar invertido: "))
            interes_compuesto()
            capital_nuevo=round((capital_inicial+interes_compuesto()),2)
            print("...")
            print("...")
            print("...")
            print(f'Bueno {nombre}, repasemos la info que me diste. Una inversion inicial de ${capital_inicial}, con una Tasa Nominal Anual de {tasa_anual}%, con una capitalizacion {plazo}, es decir que los intereses se van a reenvertir {plazo.upper()}MENTE, los interes seran de {round((interes_compuesto()),2)}. Tu inversion con el interes compuesto en el plazo de {int(t)} años, ascendera a {capital_nuevo}')
            break
        except:#funciona
            print(f'{nombre} por favor ingresa solo valores numericos')#funciona
    seguir=True
    while seguir==True:
        try:
            print("")
            usar=str(input(f'{nombre}, ¿queres volver a usar la calculadora?\n1.Si\n2.No\n')).title()
        except:
            print(f'{nombre}, ingresa alguna de las opciones dadas')
        if usar=="No":#funciona
            print("")
            print("Adios")
            print("Un placer haberte ayudado")
            print(f'{nombre}, nos vemos')
            print("Adios")
            uso=False
            break
        elif usar=="Si":
            try:
                capital_inicial=float(input("Ingresa tu inversion incial: "))
                tasa_anual=int(input("Ingresa la Tasa Nominal Anual: "))
                tiempo=True
                while tiempo==True:
                    try:
                        n=str(input("Ingresa el plazo de capitalizacion de los interes.\n1.Anual\n2.Semestral\n3.Trimestral\n4.Mensual\n")).title()
                    except:
                        print(f'Por favor {nombre}, elegi un de las opciones validas')
                    if n=="Anual":
                        n=1
                        plazo="Anual"
                        break
                    elif n=="Semestral":
                        n=2
                        plazo="Semestral"
                        break
                    elif n=="Trimestral":
                        n=4
                        plazo="Trimestral"
                        break
                    elif n=="Mensual":
                        n=12
                        plazo="Mensual"
                        break
                    else:
                        print(f'por favor {nombre}, elegi un de las opciones validas')
                t=float(input("Ingresa la cantidad de años que vas a dejarlo: "))
                interes_compuesto()
                capital_nuevo=round((capital_inicial+interes_compuesto()),2)
                print("...")
                print("...")
                print("...")
                print(f'Bueno {nombre}, repasemos la info que me diste. Una inversion inicial de ${capital_inicial}, con una Tasa Nominal Anual de {tasa_anual}%, con una capitalizacion {plazo}, es decir que los intereses se van a reenvertir {plazo.upper()}MENTE, los interes seran de {round((interes_compuesto()),2)}. Tu inversion con el interes compuesto en el plazo de {int(t)} años, ascendera a {capital_nuevo}')
            except:#funciona
                print(f'{nombre} por favor ingresa solo valores numericos')#funciona
        else:
            print(f'Por favor {nombre}, elegi alguna de las dos opciones')
