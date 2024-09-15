"""
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía de un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse la
conversión de datos
- Identificar si la edad es mayor de 30 mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10
de su sueldo, según corresponda
"""

nombre = "Joao Chavez"
salario = 3500
edad = "27"
compañia = "UNMSM"



if int(edad) > 30:
    bono_10 = (salario**2) + (salario*0.10)
    print("Usted tiene un bono del 10% en el mes de diciembre")
    print(f"El total de su bono es de: {bono_10} soles")

else:
    bono_5 = (salario**2) + (salario*0.5)
    print("Usted tiene un bono del 5% en el mes de diciembre")
    print(f"El total de su bono es de: {bono_5} soles")