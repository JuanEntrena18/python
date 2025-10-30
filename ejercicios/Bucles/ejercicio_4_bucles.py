#Ejercicio 4 
#Escribir un programa que pida al usuario un número entero positivo y muestre por 
#pantalla la cuenta atrás desde ese número hasta cero separados por comas.
numero_usuario = int (input("Dime un número y hago una cuenta atras"))
contador = numero_usuario
while contador >= 0:
    print (contador, end=", ")
    contador -= 1
    
   

