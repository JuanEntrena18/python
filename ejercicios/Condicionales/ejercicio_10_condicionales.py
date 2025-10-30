#Ejercicio 10 
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
#Los ingredientes para cada tipo de pizza aparecen a continuación. 
#●  Ingredientes vegetarianos: Pimiento y tofu. 
#●  Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. 
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y 
#en función de su respuesta le muestre un menú con los ingredientes disponibles 
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el 
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la 
#pizza elegida es vegetariana o no y todos los ingredientes que lleva
pizza = int(input("Bienvenido al cajero pizzero Bella Napoli.\nDime si quieres una pizza vegetariana o no.\nSi la quieres vegetariana pulsa [1] si no, pulsa [0] "))
vegetariana = int(1)
no_vegetariana = int(0)
if (pizza == 1):
    seleccion_temp=int(input("Has seleccionado vegetariana. Tu pizza lleva tomate y mozzarela, añade un ingrediente más puede ser pimiento [2] o tofu [3]"))
    if (seleccion_temp == 2):
        print ("Has seleccionado una pizza vegetariana con mozzarela, tomate y pimiento")
    else:
        print ("Has seleccionado una pizza vegetariana con tomate, mozzarela y tofu")
elif (pizza ==0):
    seleccion_temp=int(input("Has seleccionado no vegetariana. Tu pizza lleva tomate y mozzarela, añade un ingrediente más puede ser peperoni [4], jamón [5] o salmón [6]"))
    if (seleccion_temp == 4):
        print ("Has seleccionado una pizza no vegetariana con mozzarela, tomate y peperoni")
    elif (seleccion_temp == 5):
        print ("Has seleccionado una pizza no vegetariana con mozzarela, tomate y jamón")
    elif (seleccion_temp == 6):
        print ("Has seleccionado una pizza no vegetariana con mozzarela, tomate y salmón")
else:
    print ("No has seleccionado un número válido")

