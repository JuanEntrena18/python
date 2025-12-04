#Ejercicio 4 
#Escribir un programa que pregunte al usuario los números ganadores de la lotería 
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor 
#a mayor.
num_ganadores = []
for i in range(6):
    temp = int(input("Dime los 6 números ganadores " + str(i+1) + ": "))
    num_ganadores.append(temp)
num_ganadores.sort()
print ("Los números ganadores son: ", *num_ganadores)
