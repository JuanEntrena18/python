#Ejercicio 7 
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las 
#letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista 
#resultante. 
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
## uso de enumerate de la lista abc para que empiece en el 1
resultado = [letra for i, letra in enumerate(abc, start=1) if i % 3 != 0]
print("El resultado es", *resultado)
