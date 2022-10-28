#Inicio del juego
print("Bienvenido a la isla, tu misión es encontrar el tesoro")

#Primer Obstaculo
direccion = (input("En el punto de salida me encuentro dos caminos en el mapa. ¿Que camino eligo?: "))

if(direccion == "izquierda"):
    print("Avanzas por el camino hasta toparte con un rio")
else:
    print("Caes en un agujero, Game over")
    exit()

#Segundo obstaculo
rio = (input("¿Nadar por el rio o esperar a que seque?: "))

if(rio == "esperar"):
    print("El rio se seca y porfin puedes pasar")
else:
    print("Eres atrapado por una tribu, game over")
    exit()
    
#Ultimo obstaculo
print("Después de seguir su recorrido entra a un túnel donde tiene varias puertas de colores")
puerta = (input("¿Elegir puerta roja, amarilla o azul?: "))

if(puerta == "azul"):
    print("Entraste por la puerta correcta, ganaste el tesoro :D")
elif(puerta == "roja"):
    print("Caes desde un abismo, game over")
elif(puerta == "amarilla"):
    print("eres devorado, game over")
else:
    print("eres asesinado, over")
    
