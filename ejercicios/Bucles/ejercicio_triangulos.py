veces = int(input("Dime la altura del triangulo "))
simbolo = input("Dime el simbolo ")
espacio = " "
for i in range(0,veces + 1, 1):
    print (espacio * i, simbolo)
for i in range(veces -1, -1, -1):
    print (espacio * i, simbolo)


