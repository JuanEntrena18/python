#Ejercicio 11 
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de 
#interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de 
#año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que 
#comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
#la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada 
#cantidad a dos decimales.
ahorros=float(input("¿Cuánto dinero tienes ahorrado? "))
interes=round(ahorros*4/100,2)

print ("El interés en el primer año es ",interes, "y tu total es ", ahorros+interes, "euros")
print ("El interés en el primer año es ",interes*2, "y tu total es ", ahorros+interes*2, "euros")
print ("El interés en el primer año es ",interes*3, "y tu total es ", ahorros+interes*3, "euros")

