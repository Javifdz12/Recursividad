import pandas as pd
import numpy as np
def creardiccionario():
    n = int(input('¿De cuantas palabras consta nuestro diccionario?\n'))
    diccionario = []
    for i in range(n):
        palabra = input(f'{i} - ')
        while palabra in diccionario:
            palabra = input('Introduce una palabra que sea nueva por favor:\n')
        diccionario.append(palabra)
    
    return diccionario
def orden(diccionario):
    n = len(diccionario)
    anterior = [0]*n
    siguiente = [0]*n
    # Ordenamos el diccionario
    diccionario_ordenado = sorted(diccionario)
    
    # La anterior a la primera palabra seá la última
    temp = diccionario.index(diccionario_ordenado[-1])
    # La posterior a la última palabra será la primera
    temp2 = diccionario.index(diccionario_ordenado[0])
    
    for i in range(n):
        for j in range(n):
            if diccionario[j] == diccionario_ordenado[i]:
                anterior[j] = temp
                temp = j
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if diccionario[j] == diccionario_ordenado[i]:
                siguiente[j] = temp2
                temp2 = j
    
    tabla = pd.DataFrame()
    tabla['diccionario'] = diccionario
    tabla['anterior'] = anterior
    tabla['siguiente'] = siguiente
    
    return tabla

def buscar(lista, dato, i = 0, nueva = list()):
    if i != len(lista):
        if dato in lista[i]:
            nueva.append(lista[i])
        i += 1
        buscar(lista, dato, i, nueva)
    return nueva

diccionario = creardiccionario()
print('\nAsí quedaría nuestro diccionario:\n')
tabla = orden(diccionario)
print(orden(diccionario))

opcion = int(input('\n\nBien hecho, ahora que desea hacer:\n\t1) Localizar palabras que contengan lo que quiero. \n\t2) Añadir nueva palabra. \n\t3) Eliminar una de las palabras. \n\t4) Crear un nuevo diccionario. \n\t5) Mostrar diccionario\nIntroduce una opción:'))
while  0 < opcion < 6:
    if opcion == 1:
        dato = input('\n¿Que deseas buscar en el diccinario?')
        diccionario_nuevo = buscar(diccionario, dato)
        if diccionario_nuevo == []:
            print('No he podido encontrar nada')
        else:
            print('Esto es lo que he encontrado\n')
            print(orden(diccionario_nuevo))

    elif opcion == 2:
        palabra = input(f'\nIntroduce una nueva palabra\n {len(diccionario)} - ')

        while palabra in diccionario:
            palabra = input('Introduce una palabra que no exista todavía por favor:\n')

        diccionario.append(palabra)
        tabla = orden(diccionario)

    elif opcion == 3:
        print(tabla)
        posicion = int(input('Posición de la palabra que desea eliminar:'))
        diccionario.pop(posicion)
        tabla = orden(diccionario)

    elif opcion == 4:
        diccionario = creardiccionario()
        tabla = orden(diccionario)

    else:
        print('\nAsí quedaría nuestro diccionario:\n')
        print(tabla)

    opcion = int(input('\n\nBien hecho, ahora que desea hacer:\n\t1) Localizar palabras que contengan lo que quiero. \n\t2) Añadir nueva palabra. \n\t3) Eliminar una de las palabras. \n\t4) Crear un nuevo diccionario. \n\t5) Mostrar diccionario\nIntroduce una opción:'))
