class animales:
    def terrestre(self):
        return True
class felino (animales):
    @property
    def garras(self):
        return True
    def cazar(self):
        print("el felino esta cazando")

class mascota:
    nombre = ""
    def mostrar_nombre(self):
        print(self.nombre)

class gato(felino,mascota):
    pass

class jaguar(felino):
    pass


Gato = gato()

Jaguar = jaguar()
print (Gato.terrestre())
print(Gato.cazar())
Gato.nombre = "pepe"
print(Gato.nombre)