import random

jug_1 = int(input("Ingrese un numero."))

acierto = 0
intentos = 5

def ganaste (jug_1,acierto):
    if acierto == 0:
        jug_2 = int(input("Adivina cual es el numero."))
        if jug_1 == jug_2:
            print("Ganaste!")
            acierto += 1
        elif jug_1 != jug_2:
            print("Incorrecto.")
            ganaste(jug_1,acierto)
    else:
        print("ganaste")

ganaste(jug_1,acierto)
jug_2 = 0

while jug_1 != jug_2 and intentos != 0:
        jug_2 = int(input("Adivina cual es el numero."))
        intentos -= 1
        print(f"Tienes {intentos} intentos.")

if jug_1 == jug_2:
    print("Ganaste!")
else:
    print("Perdiste!")
        
    
print("Blackjack!")

monto = int(input("Cual es el monto total que traes?"))

carta_c = random.randint(1,11)


while monto > 0:
    apuesta= int(input("Cuanto deseas apostar en la mano?"))
    monto -= apuesta
    cartas = random.randint(1,11) + random.randint(1,11)
    jug_a == random.randint(1,21)
    print(f"Sacaste un total de {cartas}")
    carta_c = int("Quieres una tercera carta?\n 1. Si\n 2. No.")
    if carta_c    
