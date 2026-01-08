diccionario = {"Euro":"€","Dolar":"$","Yen":"Y"}
pregunta = input("Dime una divisa y te digo su símbolo: ")
if (pregunta == "Euro"):
    print (diccionario["Euro"])
elif (pregunta == "Dolar"):
    print (diccionario["Dolar"])
elif (pregunta == "Yen"):
    print (diccionario["Yen"])
else:
    print ("No has puesto ninguna divisa")
