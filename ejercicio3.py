from random import choice
def crearlista_colores():
    n = int(input('¿cuantas colores quieres?'))
    lista = []
    print(f'Introduce {n} colores a la lista de fichas:')
    for i in range(n):
        lista.append(str(input(f'{i+1} - ').lower()))
    return lista
colores=crearlista_colores()
print(colores)

a=int(input("¿De cuantas fichas quieres el juego?"))
fichas_sin_colocar=[]
for i in range(a):
    fichas_sin_colocar.append(choice(colores))
print(fichas_sin_colocar)


fichas_frecuencia={"rojo":0,"verde":0,"azul":0}
for c in fichas_sin_colocar:
    if c in fichas_frecuencia:
        fichas_frecuencia[c]+=1
    else:
        fichas_frecuencia[c]=1
          
print(fichas_frecuencia)

    
fichas_rojas=[]
for i in range(fichas_frecuencia["rojo"]):
    fichas_rojas.append("rojo")

print(fichas_rojas)
fichas_verdes=[]
for i in range(fichas_frecuencia["verde"]):
    fichas_verdes.append("verde")
print(fichas_verdes)
fichas_azules=[]
for i in range(fichas_frecuencia["azul"]):
    fichas_azules.append("azul")
print(fichas_azules)

x=fichas_frecuencia["rojo"]+fichas_frecuencia["verde"]+fichas_frecuencia["azul"]
y=len(fichas_sin_colocar)-x
fichas_otros_colores=[]
for i in range(y):
    fichas_otros_colores.append("otro color")
print(fichas_otros_colores)

def ordenar(lista):
    fichas_frecuencia={"rojo":0,"verde":0,"azul":0}
    for c in lista:
        if c in fichas_frecuencia:
            fichas_frecuencia[c]+=1
        else:
            fichas_frecuencia[c]=1



    fichas_rojas=[]
    for i in range(fichas_frecuencia["rojo"]):
        fichas_rojas.append("rojo")


    fichas_verdes=[]
    for i in range(fichas_frecuencia["verde"]):
        fichas_verdes.append("verde")

    fichas_azules=[]
    for i in range(fichas_frecuencia["azul"]):
        fichas_azules.append("azul")


    x=fichas_frecuencia["rojo"]+fichas_frecuencia["verde"]+fichas_frecuencia["azul"]
    y=len(lista)-x
    fichas_otros_colores=[]
    for i in range(y):
        fichas_otros_colores.append("otro color")


    return fichas_rojas+fichas_verdes+fichas_azules+fichas_otros_colores


fichas_ordenadas=ordenar(fichas_sin_colocar)
print(fichas_ordenadas)

def crearlista_colores():
    n = int(input('¿cuantos colores quieres?'))
    lista = []
    print(f'Introduce {n} colores a la lista de fichas:')
    for i in range(n):
        lista.append(str(input(f'{i+1} - ').lower()))
    return lista
colores=crearlista_colores()
print(colores)

a=int(input("¿De cuantas fichas quieres el juego?"))
fichas_sin_colocar=[]
for i in range(a):
    fichas_sin_colocar.append(choice(colores))
print(fichas_sin_colocar)



def colocar_fichas(lista,i=0):

    fichas_rojas = []
    fichas_verdes = []
    fichas_azules = []
    no_pertenece = 0
    while i != len(lista):
        if lista[i] == "rojo":
            fichas_rojas.append(lista[i])
            i += 1
            colocar_fichas(lista,i)
        elif lista[i] == "verde":
            fichas_verdes.append(lista[i])
            i += 1
            colocar_fichas(lista,i)
        elif lista[i] == "azul":
            fichas_azules.append(lista[i])
            i += 1
            colocar_fichas(lista,i)
        else:
            no_pertenece += 1
            i += 1
            colocar_fichas(lista,i)
    return fichas_rojas+fichas_verdes+fichas_azules

fichas_ordenadas2=colocar_fichas(fichas_sin_colocar)
print(fichas_ordenadas2)