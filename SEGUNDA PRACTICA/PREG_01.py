"""
1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana y un método para solicitar su nombre
y edad. OK
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método aumentoSueldo
para incrementar su sueldo en un 30% (mínimo instanciar la clase 2 veces,
mostrar por pantalla dicho sueldo ya incrementado).
- Crear un método que retorne un mensaje donde indique que: “En el año
2025 tendrá XX años”, el año se ingresará por parámetro y la edad es la
edad que ya se ingresó (Mostrar por pantalla este valor)

"""

class Persona:

    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.__saldo = 0
        self.sueldo = 0
        self.nacionalidad = "Peruana"


    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))
        self.sueldo = int(input("Ingrese su sueldo: "))


    def cumple(self):
        self.edad = self.edad + 1
        print(f"Feliz cumpleaños tu edad actual es {self.edad}")

    def aumento_sueldo(self):
        self.sueldo = self.sueldo * 1.30
        print(f"Tuviste un aumento de sueldo, tu sueldo actual es {self.sueldo}")

    def edad_nueva(self, año):
        self.edad_año = self.edad + (año - 2024)
        return f"En el año {año} tendrás {self.edad_año} años"


persona1 = Persona()
persona1.solicitar_datos()
persona1.aumento_sueldo()
persona1.aumento_sueldo()
print (persona1.edad_nueva(2025))
