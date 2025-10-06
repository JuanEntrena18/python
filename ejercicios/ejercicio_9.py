#Ejercicio 9 
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
#y el número de años, y muestre por pantalla el capital obtenido en la inversión. 
cantidad=float(input("Introduce el capital inicial a invertir: "))
interes=float(input("Introduce el interés, sólo número:"))
tiempo=float(input("¿Cuantos años vas a tener el dinero en el banco?"))
interesTotal=round(cantidad*((1+interes/100),tiempo),2)
print("El capital a obtener será de: ", +str(interesTotal))