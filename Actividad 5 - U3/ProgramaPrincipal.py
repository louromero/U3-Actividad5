from Lista import Lista

def testLista():
    lista = Lista()
    band=True
    while band:
        opcion=int(input("\nDesea ingresar un elemento (1. Si--------0.No): "))
        if opcion==1:
            num=int(input("\nIngrese elemento: "))
            lista.agregar(num)
        else:
            print("\nYA NO SE AGREGARAN MAS ELEMENTOS.")
            band=False

    posicion=int(input("\nIngrese numero de posicion para mostrar elemento: "))
    lista.mostrar(posicion)

    pos=int(input("\nPosicion donde quiera ingresar elemento: "))
    num=int(input("Ingrese elemento que quiera ingresar: "))
    lista.insertar(pos,num)
    lista.mostrar(pos)

    #Al exceder el rango, lo ingresa al final
    lista.insertar(56,7)
    lista.mostrar("..")
    lista.mostrar(56)

    print(" ")
    print(lista)
    print(" ")

if __name__ == '__main__':
    testLista()