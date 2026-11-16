#Generar intervalos  
import time
import random
def generar_intervalos(cantidad):
    elemntos = [
        max(1, cantidad // 4),
        max(1, cantidad // 2),
        cantidad
    ]
    return sorted(set(elemntos))

#Generar numeros
def generar_numeros(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(1, 5_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo
cantidad = int(input("Cantidad de elementos: "))
datos, tiempo = generar_numeros(cantidad)
print("Iniciar generación.")
print(f"Tiempo en ejecución: {tiempo:.4f}")
print("Fin de generación.")
ini = time.perf_counter()
print(datos)
fin = time.perf_counter()
dif = fin - ini
print(f"Tiempo de ejecución: {tiempo:.4f}")
print(f"Duracion de impresión: {dif:.4f}")
 
#Ordenamiento burbuja
def ordenamiento_burbuja(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n-i-1):
            if datos[j] > datos[j+1]:
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos
