#Ejercicio 8 
#En una determinada empresa, sus empleados son evaluados al final de cada año. 
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir 
#aumentando, traduciéndose en mejores beneficios. Los puntos que pueden 
#conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores 
#intermedios entre las cifras mencionadas. A continuación se muestra una tabla con 
#los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida 
#en cada nivel es de 2.400€ multiplicada por la puntuación del nivel. 
#Nivel  Puntuación 
#Inaceptable  0.0 
#Aceptable  0.4 
#Meritorio  0.6 o más 
#Escribir un programa que lea la puntuación del usuario e indique su nivel de 
#rendimiento, así como la cantidad de dinero que recibirá el usuario. 
dinero_nivel = float(2400)
puntos_usuario = float(input("¿Cuántos puntos has conseguido este mes?"))
sobresueldo = puntos_usuario * dinero_nivel
if (puntos_usuario == 0.0):
    print ("Este mes no tienes sobresueldo")
elif (puntos_usuario == 0.2):
    print ("Este mes has conseguido un sobresueldo de", sobresueldo, "euros")
elif (puntos_usuario == 0.4):
    print ("Este mes has conseguido un sobresueldo de", sobresueldo, "euros")
elif (puntos_usuario == 0.6):
    print ("Este mes has conseguido un sobresueldo de", sobresueldo, "euros")
elif (puntos_usuario == 0.8):
    print ("Este mes has conseguido un sobresueldo de", sobresueldo, "euros")
elif (puntos_usuario == 1):
    print ("Este mes has conseguido un sobresueldo de", sobresueldo, "euros")
else:
    print ("Has introducido un nivel de puntos que no es válido")

