import os
diccionario = ()
sw = True
def fnt_agregar(diccionario, placa, descripcion_vehiculo, nombre, contacto, ruta, descripcion_carga):
     if placa == '' or descripcion_vehiculo == '' or nombre == '' or contacto == '' or ruta == '' or descripcion_carga == '':
         enter = input('No se puede agregar un vehiculo sin datos <ENTER>')
         
     else:
         diccionario[placa] = {'Descripcion del vehiculo': descripcion_vehiculo, 'Nombre': nombre, 'Contacto': contacto, 'Ruta': ruta, 'descripcion de la carga': descripcion_carga}
         diccionario += 1
         enter = input(f'\n La persona {nombre} ha sido registrada con éxito <ENTER>')

def fnt_selector(op):
    if op == 1:
        os.system('cls')
        placa = input('Ingrese la placa del vehiculo: ')
        descripcion_vehiculo = input('Ingrese la descripcion del vehiculo: ')
        nombre = input('Ingrese el nombre del conductor: ')
        contacto = input('Ingrese el contacto del conductor: ')
        ruta = input('Ingrese la ruta del vehiculo: ')
        descripcion_carga = input('Ingrese la descripcion de la carga: ')

        fnt_agregar(diccionario, placa, descripcion_vehiculo, nombre, contacto, ruta, descripcion_carga)


