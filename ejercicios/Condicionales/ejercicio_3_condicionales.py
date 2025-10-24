#Ejercicio 3 
#Escribir un programa que pida al usuario dos números y muestre por pantalla su 
#división. Si el divisor es cero el programa debe mostrar un error.
numero1=int(input("Introduce el primer número "))
numero2=int(input("Introduce el segundo número "))
division = numero1 / numero2
if numero1 == 0 or numero2 == 0:
    print ("El divisor es cero")
else:
    print ("La división es: ",division)