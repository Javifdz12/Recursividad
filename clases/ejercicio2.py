import unicodedata
import sys

def palindromo(x):
    x=x.lower()
    x=x.replace(" ","")
    caracteres=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    x_normalizado=unicodedata.normalize("NFD",x)
    x=x_normalizado.translate(caracteres)
    print(x)
    longitud=len(x)
    if longitud%2==0:
        izquierda=x[:longitud//2]
        derecha=x[longitud//2:]
        print(izquierda)
        print(derecha)
        return izquierda==derecha[::-1]
    else:
        izquierda=x[:longitud//2]
        derecha=x[longitud//2+1:]
        print(izquierda)
        print(derecha)
        return izquierda==derecha[::-1]


print(palindromo("Atar a la rata"))

def normalizar(x):
    x=x.lower()
    x=x.replace(" ","")
    caracteres=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    x_normalizado=unicodedata.normalize("NFD",x)
    x=x_normalizado.translate(caracteres)
    return x

frase=str(input("escribe algo: "))
frase=normalizar(frase)
print(frase)

def palindromo2(frase,i=0,j=-1,a=True):

    for i in range(len(frase)-1):
        if frase[i] != frase[j]:
            a = False
        else:
            if j==-len(frase):
                a=True
            else:
                j -= 1
                palindromo2(frase, i, j, a)
    return a



print(palindromo2(frase))


