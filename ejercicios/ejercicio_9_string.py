#Ejercicio 9 
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato 
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa 
#anterior para que también funcione cuando el día o el mes se introduzcan con un 
#solo carácter.
fecha_usuario=str(input("Introduce tu fecha de nacimiento con este formato dd/mm/aaaa " ))
fecha_corta=fecha_usuario.split("/")
print ("El día es",fecha_corta[0],"el mes es",fecha_corta[1], "el año es", fecha_corta[2])

