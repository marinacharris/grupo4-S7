archivo1 = open('TextoPrueba.txt', 'rt') #así abre de solo lectura
# w: escribir, abre un archivo para escribir, si no existe el archivo lo crea
# r: leer, abre un archivo para lectura y es el valor por defecto, si el archivo no existe sale error
# a: agregar, abre un archivo para agregar y crea el archivo si no existe
for i in archivo1:
    print(i)

print(archivo1.readline())
print(archivo1.readlines())
print(archivo1.read()) # se leen los primeros 10 caracteres

archivo1.close()

archivo2 = open('TextoPrueba2.txt', 'w')
archivo2.write('Hello World2 \n')
archivo2.close()
archivo2 = open('TextoPrueba2.txt', 'a')
archivo2.write('Hello World2 \n')
archivo2.close()

lista = ['Marina','Oscar','Juan','Sofía','Laura']
archivo3 = open('TextoPrueba3.txt', 'w', encoding='utf-8')
for i in lista:
    archivo3.write(i)
    archivo3.write('\n')
archivo3.close()

    


