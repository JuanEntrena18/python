#Ejercicio 6 
#Escribir un programa que pida al usuario un número entero y muestre por pantalla 
#un triángulo rectángulo como el de más abajo, de altura el número introducido. 
#* 
#** 
#*** 
#**** 
#*****
numero = int(input("Introduce un número y te hago un árbolito de navidad "))
contador = 1
while contador <= numero :
    print ("*" *contador)
    contador = contador +1
