"""
2. Usando el concepto de herencia y encapsulación (para saldo) para crear
elsiguiente programa (3 ptos):
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas.

"""

class Persona1:

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
        self.__saldo = int(input("Ingrese su saldo actual: "))


    def cumple(self):
        self.edad = self.edad + 1
        print(f"Feliz cumpleaños tu edad actual es {self.edad}")

    def aumento_sueldo(self):
        self.sueldo = self.sueldo * 1.30
        print(f"Tuviste un aumento de sueldo, tu sueldo actual es {self.sueldo}")

    def edad_nueva(self, año):
        self.edad_año = self.edad + (año - 2024)
        return f"En el año {año} tendrás {self.edad_año} años"

    def mostrar_saldo(self):
        print(f"Hola {self.nombre} tu saldo actual es de {self.__saldo}")

    def transferencia(self, monto, persona_a_transferir):
        if monto > self.__saldo:
            print("Su saldo es insuficiente")
        else:
            self.__saldo = self.__saldo - monto
            persona_a_transferir.__saldo = persona_a_transferir.__saldo + monto
            print("Transferencia realizada")
            print(f"Monto transferido: {monto}")



class Persona2(Persona1):
    def __init__(self):
        super().__init__()

    def solicitar_datos(self):
        super().solicitar_datos()


persona1 = Persona1()
persona2 = Persona2()

print("Datos de persona1")
persona1.solicitar_datos()

print("Datos de persona2")
persona2.solicitar_datos()

print("Transferencia de dinero persona1 a persona2")
persona1.transferencia(1000, persona2)

print("Saldo persona1")
persona1.mostrar_saldo()

print("Saldo persona2")
persona2.mostrar_saldo()