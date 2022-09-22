from optparse import Values


print("Bienvenido\n"
       "Elija la opcion de acuerdo a su necesidad\n"
       "Opcion 1: Consultar precio de una fruta\n"
       "Opcion 2: Agregrar fruta\n"
       "Opcion 3: Modificar fruta o precio\n"
       "Opcion 4: Borrar fruta\n"
       "Opcion 5: Listar frutas y precios\n"
       "opcion 6: Inventario (cantidad de frutas y promedio de precios\n"
       "Opcion 7: Salir")

frutas={'pera': 2000,
        'uvas': 8000,
        'banano': 500,
        'fresas': 3000,
        'manzana': 1500
        }


while True:
    opcion=int(input("Elija la opcion: "))
    if opcion==1:
        fruta=(input("ingrese fruta: ")).lower()
       
        print(f'el valor de la {fruta} es: ', frutas.get(fruta, "esa fruta no es vendida en la tienda"))
            



    if opcion==2:
        fruta=input("ingrese la fruta que desea agregar: ").lower()
        if fruta in frutas:
            print("la fruta ya es vendida en la tienda")
        
        else:
            precio=int(input("ingrese el valor de la fruta: "))
            frutas[fruta]=precio
            print("la fruta se agrego a la tienda")

    if opcion==3:
        fruta=input("ingrese la fruta que desea modificar: ")
        if fruta in frutas:
            precio=float(input("ingrese el nuevo precio de la fruta: "))
            frutas[fruta]=precio
            print("el precio de la fruta", fruta, "ha cambiado")

        else:
            print("la fruta no es vendida en la tienda")
            print("lista de frutas y precios", frutas)

    if opcion==4:
        fruta=input("ingrese la fruta que desea eliminar de la tienda: ")
        if fruta in frutas:
            del (frutas[fruta])
            print(f'las {fruta} se ha eliminado de la tienda')
            
        else:
            print("la fruta no es vendida en la tienda")
            print(frutas)

    if opcion==5:
        for i in frutas.items():
            print([i])

    if opcion==6:
        print(f'la tienda tiene {len(frutas)} frutas')
        print("la suma de los valores de las frutas es: ", sum(frutas.values()))
        promedio=sum(frutas.values())//len(frutas)
        print("el promedio es :", promedio)


    if opcion==7:
        print("Fin del accion.....saliendo")
        break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    












       