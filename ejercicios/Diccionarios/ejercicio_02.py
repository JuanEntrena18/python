#Ejercicio 2
#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
#y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
#<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>.
nombre = str(input("¿Cuál es tu nombre? "))
edad = int(input("¿Cuál es tu edad? "))
direccion = str(input("¿Cúal es tu dirección? "))
telefono = input("¿Cuál es tu teléfono? ")

diccionario = {
    "nombre":nombre,
    "edad":edad,
    "direccion":direccion,
    "telefono":telefono
}

print (f"{diccionario["nombre"]} tienes {diccionario["edad"]} vives en {diccionario["direccion"]} y tu teléfono es {diccionario["telefono"]}")