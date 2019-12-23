class animal:
    volador = True
class cocodrilo(animal):

   
   def __init__(self,nombre):
       self.nombre = nombre
       
   @classmethod
   def new(self,nombre):
       return cocodrilo(nombre)

crocro = cocodrilo.new("coco")