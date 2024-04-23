mi_diccionario = {}
import os
sw = True

numero_compras = 0
def fnt_compras ():
    global numero_compras
def fnt_agregar(mi_diccionario, nombre, direccion, contacto, sexo, descripcion, producto, referencia, cantidad, numero_compras):
    if nombre == '' or direccion == '' or contacto == '' or sexo == '' or descripcion == '' or cantidad == '' or producto == '' or referencia == '' or cantidad == '':
        enter = input('Debe diligenciar toda la informacion >ENTER<')
    else:
        mi_diccionario[nombre] = {' CLIENTE:' ,nombre }
        numero_compras += 1
                 
                 
def fnt_selector(op):
    if op == '1':
        nombre = input('Ingrese su nombre:  ')
        direccion = input('Ingrese su direccion:  ')    
        contacto = input('Ingrese su numero de contacto:   ')
        sexo = input('Ingrese su sexo(FEMENINO O MASCULINO):  ')
        descripcion = input('Agregue una descripcion del lugar donde se hara entrega el producto:  ')
        os.system('cls')
        print('Adicional a ello necesitamos otra informacion para terminar tu pedido')
        producto = input('Ingrese el nombre del producto:  ')
        referencia = input('Ingrese la referencia: ')
        cantidad = input('Ingrese la cantidad: ')
        fnt_agregar(mi_diccionario,nombre, direccion, contacto, sexo, descripcion, producto, referencia, cantidad, numero_compras)

        
    
    
        
while sw == True:
    os.system('cls')
    opcion = input('\n1. COMPRAR PRODUCTO\n2. MOSTRAR PEDIDOS REALIZADOS\n3. SALIR\n->')
    if opcion == '1':
        fnt_selector(opcion)
    if opcion == '2':
        os.system('cls')
        print('COMPRAS REALIZADAS: ' ,len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    if opcion == '3':
        sw = False
