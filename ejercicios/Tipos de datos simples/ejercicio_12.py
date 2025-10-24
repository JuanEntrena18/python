#Ejercicio 12 
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene 
#un descuento del 60%. Escribir un programa que comience leyendo el número de 
#barras vendidas que no son del día. Después el programa debe mostrar el precio 
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el 
#coste final total.
pan=float(3.49)
descuento=float(pan*60/100)
precio_final=round(float(pan-descuento),2)
barras_vendidas_desc=int(input("¿Cuántas barras de pan de ayer has vendido? "))
print ("Has vendido ", barras_vendidas_desc," barras de pan de ayer, a un precio de ", barras_vendidas_desc*precio_final) 