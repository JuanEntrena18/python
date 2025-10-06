cantidad=float(input('Introduce el capital inicial a invertir: '))
interes=float(input('Introduce el interés, sólo número:'))
tiempo=float(input('¿Cuantos años vas a tener el dinero en el banco? '))

interesTotal=round(cantidad*((1+interes/100),tiempo),2)

print("El capital a obtener será de: "+str(interesTotal))                  
1