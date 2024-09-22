"""
1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola.
"""
import random


def lista_aleatoria():
    lista1 = []
    for i in range(10):
        num = random.randint(1, 10)
        lista1.append(num)
    print(f"La lista aleatoria es: {lista1}")
    return lista1


def num_unicos(lista1):
    unicos = []
    for i in range(len(lista1)):
        if lista1.count(lista1[i]) == 1:
            unicos.append(lista1[i])
    print(f"Números únicos de la lista {unicos}")
    return unicos


def mayor_menor(unicos):
    list_may = sorted(unicos, reverse=True)
    list_men = sorted(unicos)
    lista_mayor = list_may
    lista_menor = list_men
    print(f"La lista de numeros unicos fue ordenada "
          f"de mayor a menor {lista_mayor}")
    print(f"La lista de numeros unicos fue ordenada "
          f"de menor a mayor {lista_menor}")
    return lista_mayor, lista_menor


def mayor_par(unicos):
    pares_unicos = []
    for i in unicos:
        if i % 2 == 0:
            pares_unicos.append(i)
    mayor_par = max(pares_unicos)
    print(f"El número mayor par de la lista unicos es {mayor_par}")
    return mayor_par


aleatorios = lista_aleatoria()
n_unicos = num_unicos(aleatorios)
mayor_menor(n_unicos)
mayor_par(n_unicos)
