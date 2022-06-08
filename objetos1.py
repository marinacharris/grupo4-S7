# Programación orientada a objetos POO
# Python es un lenguaje orientado a objetos
# En Python casi todo es un objeto
# Una clase es un modelo o patrón o plantilla de la cual se crean objetos
# Hay que declara o crear una clase antes de porder crear los objetos
# Al crear una clase se definen:
#   los atributos o propiedades -> variables
#   los métodos -> funciones
# Al crear un onjeto de una clase, es lo mismo que decur: "crear una 
# INSTANCIA de una clase"

#Crear una clase
class Persona:
    def crear(self, nombre:str):
        self.name = nombre
    
    def mostrar(self)->str:
        return self.name
    
x = Persona()
print(type(x))

x.crear('María')
x.name = 'Juan'
print(x.mostrar())

    
    
    


