# def es_primo(numero):
#     if numero < 2:
#         return False
#     for i in range(2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             return False
#     return True

# def guardar_primos_en_archivo(inicio, fin, nombre_archivo):
#     with open(nombre_archivo, 'w') as archivo:
#         for numero in range(inicio, fin + 1):
#             if es_primo(numero):
#                 archivo.write(f"{numero}\n")

# # Ejemplo de uso
# inicio_intervalo = 1
# fin_intervalo = 1000000000000000000000000000000
# nombre_del_archivo = "numeros_primos.txt"
# guardar_primos_en_archivo(inicio_intervalo, fin_intervalo, nombre_del_archivo)

#funciones. indentar (sangria). pass = que no ocurra nada.
#Dentro de los parentesis ponemos el argumento.

#Asi se llama a la funcion.
