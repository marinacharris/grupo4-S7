# Programación orientada a objetos POO
# Python es un lenguaje orientado a objetos
# En Python casi todo es un objeto
# Una clase es un modelo o patrón o plantilla de la cual se crean objetos
# Hay que declara o crear una clase antes de porder crear los objetos
# Al crear una clase se definen:
#   los atributos o propiedades -> variables
#   los métodos -> funciones
# Al crear un objeto de una clase, es lo mismo que decir: "crear una 
# INSTANCIA de una clase"

#Crear una clase
class Persona:
    def crear(self, nombre:str):
        self.name = nombre
    
    def mostrar(self)->str:
        return self.name
    
x = Persona() # aquí creamos el objeto
print(type(x))

x.crear('María')
x.name = 'Juan'
print(x.mostrar())

# El método __init__, es un método especial
# Este método se ejecuta automáticamente cuando se crea el objeto (el constructor)
# Y el objetivo de este método es inicializar los atributos del objeto
# Este método no retorno datos y generalmente recibe parámetros para inicializar
# algunas propiedades del objeto

class Estudiante:
    def __init__(self):
        self.nombre = input('Digite el nombre del estudiante\n')
        self.nota = float(input('Digite la nota del estudiante\n'))
    def imprimir(self):
        print('Nombre:', self.nombre)
        print('Nota:', self.nota)    
    def aprobar(self):
        if self.nota >= 3.0:
            print('Aprobó')
        else:
            print('No aprobó')
            
estudiante1 = Estudiante()
estudiante1.imprimir()
estudiante1.aprobar()

                
    
    
    


