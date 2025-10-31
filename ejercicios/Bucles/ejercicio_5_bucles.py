#Ejercicio 5 
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada 
#año que dura la inversión
cantidad = float(input("Dime la cantidad que quieres invertir "))
interes = float(input("¿Cuál es el interés anual? "))
anios = int(input("Introduce los años que vas a tener el dinero invertido "))
calculo = (cantidad * interes) / 100 * anios
contador = 1
while contador <= anios:
    dinero_anio = cantidad * (interes / 100)
    cantidad = cantidad + dinero_anio
    print ("Has ganado ",round(dinero_anio,2),"con un total de",round(cantidad,2))
    contador = contador +1
