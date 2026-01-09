#Ejercicio 3
#Escribir un programa que guarde en un diccionario los precios de las frutas de la
#tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
#precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
#mostrar un mensaje informando de ello.
#Fruta Precio
#Plátano 1.35
#Manzana 0.80
#Pera 0.85
#Naranja 0.70

frutas = {
    "Platano" : 1.35,
    "Manzana" : 0.80,
    "Pera" : 0.85,
    "Naranja" : 0.70 
}

pregunta = input("Dime una fruta ")
if pregunta in frutas:
    kilos = float(input("Dime cúantos kilos quieres "))
    precio = frutas[pregunta]
    calculo = precio * kilos
    print (f"Has comprado", kilos, "kilos de ",pregunta,"con un precio de",calculo, "€")
else:
    print ("Tu fruta no está en la lista")

