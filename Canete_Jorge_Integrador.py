#Cañete Jorge
import random as ram
import time

#Variables
diccionario= 'qwertyuiopasdfghjklñzxcvbnm1234567890'

categorias= {
    "camisas": 'camisas,camisetas, camisas de vestir, camisas informales, camisas de manga corta, manga larga',
    "pantalones": 'pantalones vaqueros, pantalones chinos, pantalones de vestir, pantalones cortos',
    "Vestidos": 'vestidos casuales, vestidos de cóctel, vestidos de noche, vestidos formales, vestidos estampados',
    "Trajes": 'trajes de dos piezas, trajes de tres piezas, trajes formales, trajes de oficina',
    "Ropa de abrigo": 'abrigos, chaquetas, chaquetones, gabardinas, chalecos',
    "Ropa deportiva": 'camisetas deportivas, pantalones deportivos, sudaderas, leggings deportivos, ropa de yoga',
    "Ropa de dormir": 'pijamas, camisones, batas, pantalones de pijama, conjuntos de dormir',
    "Accesorios": 'sombreros, gorras, bufandas,guantes,cinturones, joyas, bolsos'
}
#Listas
carrito=[] 
catalogo = set()

## cargamos el catalogo con todos los elementos de las categorias
for i in categorias:
    for x in categorias[i].split(","):
        catalogo.add(x.strip())


#####Funciones
def generador_con(diccionario,largo_con):
    #Genero la contraseña con valores aleatorios
    password=[]
    for i in range(int(largo_con)):
        password.append(ram.choice(diccionario))

    return ''.join(password)

## bloquear un minuto
def bloquear():
    print('Excedió el limite de intentos. Deberá esperar un minuto.')
    for segundos in range(0,60):
        print(f'0:{segundos}', end="\r")  
        time.sleep(1)
    print('Puede volver a intentarlo.')
    print()


def verificar_con(mostrar_con):
    #Verifico si la contraseña ingresada es la misma que tiene el usuario y si pasa el limite de intentos que espere un minuto
    contador = 5
    while True:
        intento_verificar=(input('Ingrese su contraseña: '))
        if intento_verificar != mostrar_con:
            print('Contraseña incorrecta')
            contador -= 1
            if contador == 0:
                bloquear()
                contador = 5
        else:
            break
    return 'Contraseña correcta'


###

def carrito_productos():
    productos= (""""
    "camisas": camisas,camisetas, camisas de vestir, camisas informales, camisas de manga corta, manga larga
    "pantalones": pantalones vaqueros, pantalones chinos, pantalones de vestir, pantalones cortos
    "Vestidos": vestidos casuales, vestidos de cóctel, vestidos de noche, vestidos formales, vestidos estampados
    "Trajes": trajes de dos piezas, trajes de tres piezas, trajes formales, trajes de oficina
    "Ropa de abrigo": abrigos, chaquetas, chaquetones, gabardinas, chalecos
    "Ropa deportiva": camisetas deportivas, pantalones deportivos, sudaderas, leggings deportivos, ropa de yoga
    "Ropa de dormir": pijamas, camisones, batas, pantalones de pijama, conjuntos de dormir
    "Accesorios": 'sombreros, gorras, bufandas,guantes,cinturones, joyas, bolsos
""")
    print(productos)
    while True:
        contador= 5

        productos_elegidos=input('Ingrese el producto que quiere añadir: ')
        while productos_elegidos not in catalogo:
            print('El producto ingresado no se encuentra en el catalogo, ingrese otro.')
            productos_elegidos=input('Ingrese el producto que quiere añadir: ')
            contador-= 1
            if contador == 0:
                bloquear()
                contador = 5
            
            if productos_elegidos in catalogo: 
                break

        while True:
            precio=int(input('Ingrese el precio del producto: $'))

            cantidad_producto= int(input(f'Ingrese la cantidad que quiere llevar de {productos_elegidos}: '))
            #Validaciones
            if precio< 1:
                print('El precio ingresado es inválido.')
                contador-= 1
                if contador == 0:
                    bloquear()
                    contador = 5

            if cantidad_producto< 1:
                print('La cantidad ingresada es inválida.')
                contador-= 1
                if contador == 0:
                    bloquear()
                    contador = 5
            else:
                break
        
        for i in range(cantidad_producto):
            carrito.append({"producto": productos_elegidos, "precio": precio})

        match input("Seguir agregando productos? si/no: ").lower():
            case "no": break
            case "si": continue
    print(carrito)

def ver_carrito():
    detalle_carrito = []
    productos_agregados = []
    
    for producto in carrito:
        if producto["producto"] in productos_agregados: continue
        for ca in categorias:
            if producto["producto"] in categorias[ca]:
                
                detalle_carrito.append({"producto":producto["producto"], "categoria":ca,"precio": producto["precio"], "cantidad":carrito.count(producto)})
                productos_agregados.append(producto["producto"])
                break
    
    return detalle_carrito

def borrar_productos():
    #pido el prod
    borrador=input('Ingrese que elemento quiere borrar: ')
    carrito_info = ver_carrito()
    
    productos = []
    cantidades = []

    for i in carrito_info:
        productos.append(i["producto"])
        cantidades.append(i["cantidad"])

    productos_cantidades = dict(zip(productos,cantidades))
    #zip lo usamos para juntar por indice a dos elementos de listas distintas
    #verifico si el producto ingresado esta en el carrito
    if borrador in productos:
        cant_eliminar=int(input('Ingrese la cantidad de productos a eliminar: '))
        
        if cant_eliminar > productos_cantidades[borrador]:
            print(f"{cant_eliminar} es mayor a {productos_cantidades[borrador]}, vuelva a intentarlo")
            return
        
        for n in range(cant_eliminar):
            
            for i in carrito:
                if i["producto"] == borrador:
                    carrito.remove(i)
                    break
        
        print(f"Se removieron {cant_eliminar} {borrador} del carrito")
    else:
        print(f'No existe {borrador} en el carrito')

    
def metodos_de_pago():
    print('Medio de pago')
    sumatotal= 0

    for i in carrito:
        sumatotal+= i["precio"]

    print('El total a pagar es de: $',sumatotal)
    print("""(1)-Con efectivo tiene 10(%)(diez) de descuento,
(2)-Tarjeta: Cubre el programa ahora 3 (12(%) de interés) ,6 (18(%) de interés) y 12 (36(%) de interés). 
(3)-Bitcoin: Mismo precio""")
    
    pago=input('Ingrese de que forma va a pagar: ').lower()
    if pago == "efectivo" or pago == '1':
        print("tendras un descuento de 10%")
        print(f'Pagará ${sumatotal*0.90:.2f}')
    elif pago == 'bitcoin'or pago == '3':
        print('Pagará el mismo precio.')
    elif pago =='tarjeta' or pago == '2':
        
        tarjetas_tipos_des = ("VISSA BNNA", "MASTERCARD PRV", "CENNSOCUD MNP", "CLARESEN KFC", "OFFIOTA LUCRA", "TREVVI CIR", "PUETRA COM")

        tarjetas_des = {"Domingo": 0.85*sumatotal,
                    "Lunes": 0.80*sumatotal,
                    "Martes": 0.85*sumatotal,
                    "Miercoles": 0.70*sumatotal,
                    'Jueves': 0.80*sumatotal,
                    'Viernes': 0.90*sumatotal,
                    'Sábado': 0.95*sumatotal}
        
        tarjetas = {"Domingo": "VISSA BNNA 15%",
                    "Lunes": "MASTERCARD PRV 20%",
                    "Martes": "CENNSOCUD MNP 15%",
                    "Miercoles": "CLARESEN KFC 30%",
                    'Jueves': "OFFIOTA LUCRA 20%",
                    'Viernes': "TREVVI CIR 10%",
                    'Sábado': "PUETRA COM 5%"}
        print(f'Tarjetas con descuentos: {tarjetas_tipos_des}')
        tipo_tarjeta=input('Ingrese el banco de su tarjeta: ').upper()
        dia = input('Ingrese el dia que realiza la compra: ').capitalize()
        
        if (dia in tarjetas) and (tipo_tarjeta in tarjetas_tipos_des):
            print(f"El dia {dia} con la tarjeta {tarjetas[dia]} de descuento")
            descu_hecho= tarjetas_des[dia]
            print(f'En su compra tendrá un descuento de ${sumatotal - descu_hecho:.2f}, por lo que pagará ${descu_hecho:.2f}.')

        else:
            cuotas= int(input('''Ud. puede pagar en cuotas con el programa ahora 3 (12(%) de aumento) ,6 (18(%) de aumento) y 12 (36(%) de aumento).
Ingrese una opción: '''))
            if cuotas == 3:
                print(f'Ud. pagará un recargo de ${sumatotal*0.12:.2f} y en total será ${sumatotal*1.12:.2f}')
                print(f'Lo pagará en {cuotas} de ${(sumatotal*1.12)//3:.2f}')
            elif cuotas ==6:
                print(f'Ud. pagará un recargo de ${sumatotal*0.18:.2f} y en total será ${sumatotal*1.18:.2f}')
                print(f'Lo pagará en {cuotas} de ${(sumatotal*1.18)//6:.2f}')
            elif cuotas ==12:
                print(f'Ud. pagará un recargo de ${sumatotal*0.36:.2f} y en total será ${sumatotal*1.36:.2f}')
                print(f'Lo pagará en {cuotas} de ${(sumatotal*1.36)//12:.2f}')
            elif cuotas ==1:
                print(f'Ud. pagará en total ${sumatotal} en un pago')
            else:
                print(f'No puede pagar en {cuotas} cuotas.')
    else:
        print('El medio de pago ingresado es inválido ')
                        

##Def's generador y verificador de contraseña
while True:
    print('Para ingresar a la tienda primero debe generar una clave')
    largo_con=(input('Ingrese el largo de su contraseña a generar: '))
    contador= 5
    if largo_con.isnumeric() and (int(largo_con)) > 0:
        mostrar_con=(generador_con(diccionario,largo_con))
        print(f'su contraseña generada es: {mostrar_con}')
        var_verificar=verificar_con(mostrar_con)
        print(var_verificar)
        break
    else:
        print()
        print('caracter inválido, vuelva a intentarlo')
        print()
        contador-=1
        if contador== 0:
            bloquear()
            contador = 5


def menu():
    while True:    
        print(f'{10* "*"}MENU{10* "*"}')
        opciones=int(input("""Ingrese la opción que quiera realizar: 
1.Agregar productos al carrito
2.Ver productos del carrito 
3.Eliminar producto/s 
4.Seleccionar medio de pago
5.Salir y cerrar
Opción: """))
        if opciones == 1:
            carrito_productos()
        elif opciones== 2:
            if carrito == []:
                print("No hay nada en carrito para mostrar.")
                continue
            print(ver_carrito())
        elif opciones== 3:
            if carrito == []:
                print("No hay nada en carrito para borrar.")
                continue
            borrar_productos()
        elif opciones== 4:
            if carrito == []:
                print("No hay nada en carrito para pagar.")
                continue
            metodos_de_pago()
        elif opciones== 5:
            print('Fin del programa')
            break
        else:
            print('Ingrese una opción válida')

menu()