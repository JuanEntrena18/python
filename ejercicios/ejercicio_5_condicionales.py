#Ejercicio 5 
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos 
#ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que 
#pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el 
#usuario tiene que tributar o no. 
edad=int(input("Introduce tu edad: "))
ingresos=int(input("Introduce tus ingresos "))
if edad >= 16 and ingresos >=1000:
    print ("Tienes que tributar ")
else:
    print ("Este año no tienes que pagar, no cumples por edad o ingresos ")