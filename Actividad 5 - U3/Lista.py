from zope.interface import implementer

from Interfaz import coleccion

@implementer(coleccion)
class Lista:

    __lista = []

    def __init__(self):
        self.__lista = []

    def insertar(self,pos,elemento):

        try:
            self.getlista().insert(pos,elemento)

        except IndexError:
            print("Posicion no valda")

    def agregar(self,elemento):
        self.getlista().append(elemento)

    def mostrar(self,posicion):
        lista = self.getlista()
        try:
            print("En la posicion {} se encuentra el elemento: {}".format(posicion, lista[posicion]))

        except IndexError:
            print("\nPosicion no valida")

        except TypeError:
            print("\nError: el indice debe ser un numero entero")

    def getlista(self):
        return self.__lista

    def __str__(self):
        cadena = str(self.getlista())
        return cadena