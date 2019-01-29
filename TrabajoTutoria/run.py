#Importamos los paquetes
from paquete_archivos.miarchivo import MiArchivo 
from modelado.edades import *
#Creamos un objeto de tipo archivopara leer el archivo
m = MiArchivo()
#Objeto para escribir el archivo
lista = m.obtener_informacion()
lista = [l.split(";") for l in lista]
#Declaramos una lista vacia
lista_edades =[]
#For para recorrer la lista
for d in lista:
    #objeto  de Edades que recibe 3 posiciones
    o=Edades(d[0], d[1], d[2])
    lista_edades.append(o.obtener_edad())
#Imprimimos la lista edades ordenadas
merge_sort_result = merge_sort(lista_edades) 
#Imprimimos
print(merge_sort_result)
#Cerramos el archivo
m.cerrar_archivo()



        





   

