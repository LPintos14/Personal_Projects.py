print("")
print("Bienvenidos a este pequeño juego")
print("")
jugar=True
condicion=True
jugar2=True
jugar3=True
def es_par(numero):
    if numero%2==0:
        print(f' El {numero} es Par')
    elif numero%2!=0:
        print(f'El {numero} es Impar ')

nombre=input("Para comenzar, ingresa tu nombre: ").title()
print("")
print(f'Hola {nombre}, mi nombre es PC')
print(f'Vamos a jugar a algo')
print(f'{nombre} vas a pensar en un numero y yo te voy a decir si es par o impar')
print("")


while jugar==True:
    print("¿Queres Jugar?\n1.Si\n2.No")
    respuesta=str(input(""))
    if respuesta=="No":
        print(f'Gracias por jugar {nombre}')
        print("Adios") 
        jugar=False        
    elif respuesta=="Si":
        while jugar2==True:
            try:
                numero=int(input(f'Dale\n¿Que numero estas pensando?: '))
            except:
                print(f'{nombre} elegi un numero por favor')
            else:    
                es_par(numero)
                jugar2==False
                break
        while condicion==True:
            print(f'¿Queres volver a jugar {nombre}?\n1.Si\n2.No')
            respuesta=str(input(""))
            if respuesta=="Si":
                while jugar3==True:
                    try:
                        numero=int(input(f'Dale\n¿Que numero estas pensando?: '))
                    except:    
                        print(f'{nombre} elegi un numero por favor')
                    else:
                        es_par(numero)
                        jugar3==False
                        break
            elif respuesta=="No":
                print(f'Gracias por jugar {nombre}')
                print("Adios")
                condicion=False
                jugar=False
                break
            else:
                print(f'Por Favor {nombre}, elegi entre Si o No')
    else:
        print(f'Por Favor {nombre}, elegi entre Si o No')
        
