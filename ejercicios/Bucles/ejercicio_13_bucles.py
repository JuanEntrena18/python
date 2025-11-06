#Ejercicio 13 
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
#que el usuario escriba “salir” que terminará. 

salida = ("salir")
while True:
    palabra = input("Introduce una palabra y yo te haré eco,ecooooo ")
    if palabra == "salir":
        break
    else:
        print(palabra)
 
