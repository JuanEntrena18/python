#Ejercicio 7 
#Los tramos impositivos para la declaración de la renta en un determinado país son 
#los siguientes: 
#Renta  Tipo impositivo 
#Menos de 10000€  5% 
#Entre 10000€ y 20000€  15% 
#Entre 20000€ y 35000€  20% 
#Entre 35000€ y 60000€  30% 
#Más de 60000€  45% 
 #Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla 
#el tipo impositivo que le corresponde.
cantidad=float(input("Introduce tu renta: "))
if cantidad < 10000:
    impuestos = "5%"
elif cantidad <= 20000:
    impuestos = "15%"
elif cantidad <= 35000:
    impuestos = "20%"
elif cantidad <= 60000:
    impuestos = "30%"
elif cantidad > 60000:
    impuestos = "45%"
print ("Tu renta es", impuestos)
