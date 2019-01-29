"""Dado el siguiente archivo utilizar una clase para representar cada linea del archivo luego
    utilizar unicamnete el atributo que represente la edad de cada objeto para almacenar en un arreglo 
o lista finalmente utilizar el algoritmo de combinacion para ordenar dichas edades"""
class Edades(object):
    """docstring for Edades"""
    def __init__(self, nom, ape, edad):
        
        self.mombre = nom
        self.apellido = ape
        self.edad = int(edad)

#Agregamos los metodos agregar y obtener
    def agregar_nombre(self, nom):
        self.nombres = nom
    def obtener_nombre(self):
        return self.nombres

    def agregar_apellido(self, ape):
        self.apellido = ape
    def obtener_apellido(self):
        return self.apellido

    def agregar_edad(self, edad):
        self.edad = edad
    def obtener_edad(self):
        return self.edad

    def __str__(self):
        return "%s %s %d "%(self.obtener_nombre(), self.obtener_apellido(), self.obtener_edad())

    def __repr__(self):
        return "%s %s %d %.2f "%(self.obtener_nombre(), self.obtener_apellido(), self.obtener_edad())

    
# Función merge_sort
def merge_sort(lista):
    
    if len(lista) < 2:
        return lista
    # De lo contrario, se divide en 2
    else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)

# Función merge
def merge(lista1, lista2):
    """
        merge se encargara de intercalar los elementos de las dos
        divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado

    # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]

    # Retornamos el resultados
    return result

