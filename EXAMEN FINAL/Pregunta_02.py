"""
2. (3 ptos) Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetro que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente.
- Al final de la función decorada indicar mediante un mensaje que función fue
ejecutada.
- La función que vas a crear va a capturar, edad, nombre, hora y minuto en que
fue registrado la persona (usas las librerías correspondientes)
- Crear otra función que será decorada y que calculará la media de 4 notas.

"""

from datetime import datetime


def decordadora1(funcion1):
    def decod2(*args, **kwargs):
        cantidad_parametros = len(args) + len(kwargs)
        if cantidad_parametros > 1:
            a = funcion1(*args, **kwargs)
            return a
        else:
            print("La función tiene uno o menos argumentos")
    return decod2


@decordadora1
def registro(edad, nombre):
    actual = datetime.now()
    hora_actual = actual.hour
    minuto_actual = actual.minute
    print(f"Se registro a {nombre} de {edad} años a las {hora_actual} "
          f"horas y {minuto_actual} minutos")


@decordadora1
def calcular_prom(n1, n2, n3, n4):
    prom = (n1 + n2 + n3 + n4)/4
    print(f"El promedio es: {prom}")


registro(27, "Joao")
calcular_prom(15, 20, 12, 16)

# Error de uno o menos argumentos
registro(27)
calcular_prom(15)
