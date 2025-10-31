#Ejercicio 7 
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
tabla = int(input("Introduce el número del que quieras saber la tabla de multiplicar "))
contador = 1
while contador < 10:
    resultado = tabla * contador
    print (tabla,"x",contador, "=",resultado)
    contador = contador +1
