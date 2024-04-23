mi_diccionario = {}
import os  
sw = True

numero_despacho = 0
def fnt_despacho():
    global numero_despacho

def fnt_agregar(mi_diccionario, placa, conductor, ruta, carga, numero_despacho):
    if placa == '' or conductor == '' or ruta == '' or carga == '': 
        enter = input('Debe diligenciar toda la información solicitada >ENTER<')
    else:
        mi_diccionario[placa] = {'CONDUCTOR': conductor, 'RUTA': ruta, 'CARGA': carga}
        numero_despacho += 1
        enter = input(f'\nEl vehiculo {placa} ha sido despachado con éxito')
        
        
    
def fnt_selector(op):
    if op == '1':
        placa = input('Ingrese la placa del vehiculo: ->  ')
        conductor = input('Ingrese el nombre del conductor: ->  ')
        ruta = input('Ingrese la ruta del viaje (salida-destino): ->  ')
        carga = input('Describa la carga del viaje: ->  ')
        fnt_agregar(mi_diccionario, placa, conductor, ruta, carga, numero_despacho)
        
while sw == True:
    os.system('cls')
    opcion = input('1. REGISTRAR SALIDA\n2. MOSTRAR\n3. SALIR\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
    if opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    if opcion == '3':
        sw= False

