# import sys 
# import time

# ajio =23
# for i in range(ajio):
#     time.sleep(1)
#     sys.stdout.write("\r%d"%ajio - i)
#     sys.stdout.flush()

#Clase
class Lapiz:
    def __init__(self,color,contiene_borrador,usa_grafito):
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito
    
    #METODOS
    def dibujar(self):
        print("el lapiz esta dibujando")

    def borrar(self):
        if self.validar_de_borra():
            print("el lapiz esta borrando")
        else:
            print("no tiene borra")

    def validar_de_borra(self):
        return self.contiene_borrador

#Objeto
lapiz_generico = Lapiz("verde",False,True)
print(lapiz_generico.color)
lapiz_generico.dibujar()
lapiz_generico.borrar()

class usuario:
    def __init__(self, username, password,email):
        self.username = username
        self.password = self.encriptacion(password)
        self.email = email
    def encriptacion(self,password):
        return len(password) * "#"

usuario = usuario("Rivier","LapamparaYT12", "rgrullon@ipisdosaj.edu.do")
print(usuario.__dict__)

#6Calculate the are of a circle wuith objects

class Circle:
    @staticmethod
    def pi():
        return 3.1416

    def __init__(self,radio):
        self.radio = radio
    def area(self):
        return self.radio * self.radio * Circle.pi()

circle = Circle(4)
print(circle.area())