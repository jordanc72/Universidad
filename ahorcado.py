"""import array as arr
def par_impar(vector):
     
    for i in vector:
        if i % 2 == 0:
            vec_par.append(i)
        else:
            vec_impar.append(i)


def cont_par(vec_par):
    contadorpar=len(vec_par)
    return contadorpar

def cont_impar(vec_impar):
    contadorimpar=len(vec_impar)
    return contadorimpar

vec_par= []
vec_impar=[]
vector= []
while True:
    num=(input('Ingrese un numero positivo o cero para finalizar: ')).split(',')
    if int(num) > 0:
        vector.append(num)
    elif int(num) == 0:
        print('Finalizó la carga de numeros')
        break
    else:
        print('Ingrese un valor válido')

resultado= par_impar(vector)

print(f'Hay {cont_par(vec_par)} numeros pares y {cont_impar(vec_impar)} impares')
"""

#año= 365
#bisiesto= // 4
"""def bisiesto(anio):
    if not (anio % 4) and (anio % 100 or not anio % 400):
        print('Es bisiesto')
    else:
        print('No es bisiesto')

anio=int(input('Ingrese un año: '))



bisiesto(anio)"""

#2
""""
def con_descuento(total):
    
    if total >= 300:
        return total *0.70
    elif total >= 200:
        return total *0.80
    elif total >= 100:
        return total *0.90
    else:
        return 'No hay descuento'

while True:
    total= int(input('Ingrese el total de la compra: '))
    print('tiene que pagar: ', con_descuento(total))
    if input('Ingresa "salir" o "o" para salir:') in ("salir","o"): break

con_descuento(total)
    """
"""
def conversor(cantidad,unidad):
    metro_cm= 100
    metro_pul= 39.37

    cm_mt=0.01
    cm_pul=0.3937

    pul_mt=0.0254
    pul_cm=2.54
    for i in ("metro", "centimetros", "pulgadas"):
        if i == 'metro':
            print(f'{cantidad} eqivale a',cantidad * metro_cm,'cm')
            print(f'{cantidad} eqivale a', cantidad * metro_pul,'pulgadas')
        elif i == 'centimetros':
            print(f'{cantidad} eqivale a',cantidad * cm_mt,'metros')
            print(f'{cantidad} eqivale a', cantidad * cm_pul,'pulgadas')
        else:
            print(f'{cantidad} eqivale a',cantidad * pul_mt,'metros')
            print(f'{cantidad} eqivale a', cantidad * pul_cm,'centimetros')
while True:
    cantidad= int(input('Ingrese la cantidad: '))
    unidad= input('Ingresa "metro", "centimetros" o "pulgadas" para hace la conversión, o escriba "0" para salir: ').lower()
    if cantidad == 0:
        break"""

#4

import random as ram
from PIL import Image
lista=['Escribe', 'programa', 'elija', 'aleatoriamente', 'palabra,', 'lista', 'palabras', 'predefinidas']
print('*****AHORCADO*****')
print('¡Adiniva la palabra!')

eleccion=ram.choice(lista)

pal_censurada=['_' for letra in eleccion]

cont=6

imagenes_ahorcado = [
    Image.open('/home/estudiante/Escritorio/Universidad/py/ahorcado_0.png'),
    Image.open('/home/estudiante/Escritorio/Universidad/py/ahorcado_1.png'),
    Image.open('/home/estudiante/Escritorio/Universidad/py/ahorcado_2.png'),
    Image.open('/home/estudiante/Escritorio/Universidad/py/ahorcado_3.png'),
    Image.open('/home/estudiante/Escritorio/Universidad/py/ahorcado_4.png'),
    Image.open('/home/estudiante/Escritorio/Universidad/py/ahorcado_5.png'),
    Image.open('/home/estudiante/Escritorio/Universidad/py/ahorcado_6.png')
]
    
while cont > 0:
    
    if '_' not in pal_censurada:
        print('Haz finalizado el juego!')
        break

    print(' '.join (pal_censurada))
    imagenes_ahorcado[6 - cont].show()
    letra= input('Ingrese una letra: ').lower()
    
    if letra in eleccion:
        for i, letra_en_pal in enumerate(eleccion):
            if letra_en_pal == letra:
                pal_censurada[i]= letra
        print(f'{letra} está en la palabra a adivinar!')

    else:
        print(f'{letra} no está en la palabra')
        cont -= 1
        print(f'Cantidad de intentos restantes: {cont}')

if cont == 0:
    print('Fin del programa, la palabra era:', eleccion)
    

