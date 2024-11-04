from io import open
import pickle

class Pelicula:
    def __init__(self,ID_NRO, titulo,duracion, lanzamiento):
        self.ID_NRO = ID_NRO
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(f'Se ha creado la pelicula: {self.titulo}')
        
    def __str__(self):
        print(f'{"ID":^5} {"Titulo":^10} {"Duración":^10} {"Lanzamiento":^5}')
        return f'{self.ID_NRO:^4} {self.titulo:^10} {self.duracion:^8} {self.lanzamiento:^10} '
    
    
class Catalogo:
    peliculas = []
    nro= 0
    
    def autoincremento(self):
        if len(self.peliculas) > 0 :
            p = self.peliculas[-1]
            self.nro = p.ID_NRO
        return self.nro + 1
    
    def __init__(self):
        self.cargar()
        
    def agregar(self,p):
        for t in self.peliculas:
            if p.titulo == t.titulo and p.duracion == t.duracion and p.lanzamiento == t.lanzamiento:
                if input('\nLa pelicula ingresada ya existe en el listado, desea seguir? S/N: \n').upper() == 'S':
                    break
                else:
                    return
        self.peliculas.append(p)
        self.guardar()
        
    def mostrar(self):
        if len(self.peliculas) == 0:
            print('El catalogo està vacio')
            return
        for pe in self.peliculas:
            print(pe)
            
    def cargar(self):
        arch= open('catalogo.pckl','ab+')
        arch.seek(0)
        try:
            self.peliculas = pickle.load(arch)
            
        except:
            print('El archivo está vacio')
            
        finally:
            arch.close()
            print(f'Se han cargado {len(self.peliculas)} peliculas')
            
    def guardar(self):
        arch= open('catalogo.pckl','wb+')
        pickle.dump(self.peliculas, arch)
        arch.close()
    
    def modificar(self,titulo,nuevo_titulo,nueva_duracion,nuevo_lanzamiento):
        for p in self.peliculas:
            if p.titulo == titulo:
                p.titulo =  nuevo_titulo
                p.duracion = nueva_duracion
                p.lanzamiento = nuevo_lanzamiento
                self.guardar()
                print(f'\nPelicula "{titulo}" actualizada con éxito')
                return
        print(f'\nPelicula "{titulo}" no se encuentra en el listado')

#4.Eliminar p
    def eliminar(self,titulo):
        for p in self.peliculas:
            if p.titulo == titulo:
                print(f'{"ID":^5} {"Titulo":^10} {"Duración":^10} {"Lanzamiento":^5}')
                SN= input(f'''{p.ID_NRO:^5} {p.titulo:^10} {p.duracion:^10} {p.lanzamiento:^10}
Desea eliminarla? S/N: ''').upper()
                if SN == 'S':
                    self.peliculas.remove(p)
                    self.nro -= 1
                    self.guardar()
                    print(f'\nPelicula "{titulo}" eliminada con éxito')
                else:
                    print(f'No se ha eliminado a "{titulo}"')
                return
             
        print(f'\nPelicula "{titulo}" no se encuentra en el listado\n')
    
#5 Buscar x ID
    def buscarID(self,ID):
        for num in self.peliculas:
            if num.ID_NRO == ID:
                print(f'{"ID":^5} {"Titulo":^10} {"Duración":^10} {"Lanzamiento":^5}')
                print(f'{num.ID_NRO:^5} {num.titulo:^10} {num.duracion:^10} {num.lanzamiento:^10}')
            else:
                print(f'No se ha encontrado una pelicula con {ID} como ID')
    
c=Catalogo()

#1,2(ver validaciones)

def menu():
    
    while True:
        op=input('''Ingrese una opción:
            1.Agregar película
            2.Mostrar catálogo
            3.Modificar película
            4.Eliminar película
            5. Buscar película por ID
            6. Buscar película por título
            7. Salir
            Op: ''')
        
        if op == '1':
            while True:
                try:
                    titulo= input('\nAgregue titulo de la  pelicula: ')
                    duracion= input('Duración: ')
                    estreno= input('Fecha de estreno: ')
                
                    if titulo != '' and duracion != '' and estreno != '':
                        c.agregar(Pelicula(c.autoincremento(),titulo,int(duracion),int(estreno)))
                            
                except ValueError:
                    print('Ha ingresado un valor incorrecto, vuelva a intentarlo')
                    
                sino= input('Desea seguir agregando peliculas? S/N:  ').upper()
                if sino != 'S':
                    break
        
        elif op == '2':
            c.mostrar()
            
        elif op == '3':
            while True:
                try:
                    titulo= input('\nIngrese el titulo de la pelicula: ')
                    nuevo_ti = input('Agregue nuevo titulo de la pelicula: ')
                    nueva_fe = int(input('Nueva fecha de estreno: '))
                    nueva_du = int(input('Nueva duración: '))
                    c.modificar(titulo,nuevo_ti,nueva_fe,nueva_du)
                    if nuevo_ti == '':
                        continue
                    elif nueva_fe == '':
                        continue
                    elif nueva_du == '':
                        continue
                    break
                except ValueError:
                    print('Ha ingresado un valor incorrecto, vuelva a intentarlo')
        elif op == '4':
            c.eliminar(input('\nIngrese el titulo de la  pelicula a eliminar: '))
        elif op == '5':
            numeroid = int(input('Ingrese el número ID de la pélicula: '))
            c.buscarID(numeroid)
            print('\nbuscar ID')
        elif op == '6':
            print('\nbuscar titulo')
        elif op == '7':
            print('\nFin del programa')
        else:
            print('\nIngrese una opción válida.')
            
        input('\nPresione Enter para continuar\n')


menu()
