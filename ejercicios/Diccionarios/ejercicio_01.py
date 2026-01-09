#Ejercicio 1
#Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
#'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
#símbolo o un mensaje de aviso si la divisa no está en el diccionario.
diccionario = {"Euro":"€","Dolar":"$","Yen":"¥"}
pregunta = input("Dime una divisa y te digo su símbolo: ")
if (pregunta == "Euro"):
    print (diccionario["Euro"])
elif (pregunta == "Dolar"):
    print (diccionario["Dolar"])
elif (pregunta == "Yen"):
    print (diccionario["Yen"])
else:
    print ("No has puesto ninguna divisa")
