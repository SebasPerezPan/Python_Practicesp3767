sum = int(input("numero."))
d = 2
while sum % d != 0:
    d += 1 

if d == sum:
    print("Es primo")
else:
    print("No es.")