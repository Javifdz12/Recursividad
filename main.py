from clases .ejercicio1 import creardiccionario,orden,buscar
from clases.ejercicio2 import palindromo,normalizar,palindromo2,frase
from clases.ejercicio3 import colocar_fichas,crearlista_colores,ordenar,choice

if __name__ == '__main__':
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

if __name__ == '__main__':
    print(palindromo("Atar a la rata"))
    print(palindromo2(frase))

if __name__ == '__main__':
    colores=crearlista_colores()
    print(colores)

    a=int(input("¿De cuantas fichas quieres el juego?"))
    fichas_sin_colocar=[]
    for i in range(a):
        fichas_sin_colocar.append(choice(colores))
    print(fichas_sin_colocar)

    fichas_ordenadas2=colocar_fichas(fichas_sin_colocar)
    print(fichas_ordenadas2)

    fichas_ordenadas=ordenar(fichas_sin_colocar)
    print(fichas_ordenadas)