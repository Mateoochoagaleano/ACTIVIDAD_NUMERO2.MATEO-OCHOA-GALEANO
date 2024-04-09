import os
nDespachos = 0
diccionario_despacho = {}
sw = True
def fnt_agregar(diccionario, placa, descripcion_vehiculo, nombre, contacto, ruta, descripcion_carga  ):
    global nDespachos
    if placa == '' or descripcion_vehiculo == '' or nombre == '' or contacto == '' or ruta == '' or descripcion_carga == '':
        enter = input('debe de diligenciar toda la informacion solicitadad <ENTER>')
    else :
        diccionario[placa] = {'Descipción del vehiculo': descripcion_vehiculo, 'nombre': nombre, 'contacto': contacto, 'ruta': ruta, 'descripcion de la carga': descripcion_carga}
        nDespachos += 1
    enter = input(f'\nLa persona {nombre} Ha sido registrado con exito :) <ENTER>')


def fnt_consultar():
    global diccionario_despacho
    os.system('cls')
    print('\nCantidad de registros: ',nDespachos,'\n')
    for key, valor in diccionario_despacho.items():
        print(f'Numero de placa: {key}')
        print(f'{valor}')
    enter = input('\n\nPresione ENTER para continuar...')


def fnt_selector(opcion):
    global sw
    global diccionario_despacho

    if opcion == '1':
        os.system('cls')
        nombre = input('Nombre: ')
        placa = input('placa: ')
        contacto = input('contacto: ')
        descripcion_vehiculo = input('vehiculo: ')
        descripcion_carga = input('carga: ')
        ruta = input('ruta: ')
        fnt_agregar (diccionario_despacho, placa, descripcion_vehiculo, nombre, contacto, ruta, descripcion_carga)

    elif opcion == '2':
        fnt_consultar()

    elif opcion == '3':
        sw = False



while sw == True: 
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    fnt_selector(opcion)


