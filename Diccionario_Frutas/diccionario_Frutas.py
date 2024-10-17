
print (" ") #Esta linea define el espacio para el nombre 
print ("Cristian David Salas De La O 3-W") #Esta linea define el nombre del programador 
print (" ") #Esta linea define el espacio para el nombre 
precios_frutas = {  #Esta linea define la funcion 
    "manzana": 3.0, #Esta linea define el precio de la fruta
    "banana": 2.5, #Esta linea define el precio de la fruta
    "naranja": 4.0, #Esta linea define el precio de la fruta
    "fresa": 6.0, #Esta linea define el precio de la fruta
    "uva": 8.0 #Esta linea define el precio de la fruta
} #Esta linea concluye
print("Precios de frutas por kilo:") #Esta linea define solicita el precio de las frutas
for fruta, precio in precios_frutas.items(): #Esta linea define define el if
    print(f"{fruta.capitalize()}: ${precio:.2f}") #Esta linea define el precio 
fruta_elegida = input("Ingrese la fruta que desea comprar: ").lower() #Esta linea solicita la fruta a comprar
kilos = float(input("Ingrese el número de kilos que desea comprar: ")) #Esta linea solicita los kilos 
if fruta_elegida in precios_frutas:  #Esta linea define el if
    precio_total = precios_frutas[fruta_elegida] * kilos #Esta linea define el precio total
    print(f"El precio total por {kilos} kilos de {fruta_elegida} es: ${precio_total:.2f}") #Esta linea muesttra el precio total
else: #Esta linea define que hacer si no se cumple la peticion 
    print("Lo siento, la fruta seleccionada no está disponible.") #Esta linea muestra que la fruta no esta disponible
