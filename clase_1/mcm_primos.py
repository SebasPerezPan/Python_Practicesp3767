a = int(input("Agregue el numero a descomponer."))

b = a

c = False

d = 2

divisores = [1]

while b != 1:
    if a / d == 1:
        c = True
        
    if b % d == 0:
        b = b / d
        divisores.append(d)
        d = 2
    else:
        d += 1


print(f"El numero {a} debe ser dividido por {divisores}")
if c == True:
    print(f"{a} es un numero primo.")
else:
    print(f"{a} no es un numero primo.")


print("Parte 2.\nPrueba Taller Knuth")

a = 2
b = a
d = 2
s = []

while b != 1:
    if a / d == 1:
        c = True
        
    if b % d == 0:
        b = b / d
        divisores.append(d)
        d = 2

s = range(1,100)
num_rang = [s]
prime = []

for a in s
while a < 10:
    
    if b / d == 1:
        s.append(a)
        d = 2
    elif b / d != 1:
        a = a + 1
    else:
        d += 1

print(s)