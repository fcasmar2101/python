entrada = input("Introduce los números de la muestra separados por comas: ")

numeros = []
for n in entrada.split(","):
    numeros.append(float(n))

n = len(numeros)
media = sum(numeros) / n

suma_cuadrados = 0
for x in numeros:
    suma_cuadrados += (x - media)**2

varianza = suma_cuadrados / (n - 1)

desviacion = varianza ** 0.5

print(f"La media es: {media}")
print(f"La desviación típica es: {desviacion}")