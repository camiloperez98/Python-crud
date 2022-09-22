"""
contador=1
sumanotas=0
nota=0
estudiante=input("ingrese el nombre del estudiante: ")

while contador<=5:
    nota=float(input("ingrese las notas: "))
    contador=contador+1
    sumanotas=sumanotas+nota
    promedio=sumanotas//5

print("promedio: ", promedio)

if promedio>=4.5:
    print("el estudiante", estudiante, "aprobo con un promedio de", promedio)

else:
    print("el estudiantes", estudiante, "no aprobo")
"""

"""
print("Bienvenido")
dolar=4.457
while True:
    valor=float(input("ingrese el valor que desea convertir: "))
    total=valor*dolar
    print("el valor de su cambio fue : $", total)
    aviso=input("desea realizar otro cambio?: ").lower()
    if aviso=="si":
        print()

    else:
        print("vuelva pronto")
        break
"""

iva=0.19
contador=0
cantidadProductos=int(input("ingrese la cantidad de productos que desea registar: "))

while contador<=cantidadProductos:
    producto=input("ingrese el nombre del producto: ")
    cantidad=int(input("ingrese la cantidad: "))
    ValorUnitario=float(input("ingrese el valor unitario"))
    valorCompra=cantidad*ValorUnitario
    valorCompra=valorCompra+1
    valorbruto=valorbruto+valorCompra
    valorNeto=valorbruto*0.19

print("el valor a pagar es de: ", valorNeto)


