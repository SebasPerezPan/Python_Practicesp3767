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

carta_a = random.randint(1,11)
carta_b = random.randint(1,11)
carta_c = random.randint(1,11)
total_cartas = carta_a + carta_b

print(total_cartas)
