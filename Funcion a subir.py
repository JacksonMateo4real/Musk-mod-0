#Ejercicio de Git.


def dime_apellido(nombre_completo):
    apellido = nombre_completo.split()
    return apellido[1]


indica_tu_nombre = input("Dime tu nombre y tu apellido: ")



print(dime_apellido(indica_tu_nombre))