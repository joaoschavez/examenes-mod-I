"""
3. Escribir un programa para gestionar una billetera electrónica (3 ptos):
Reglas:
- El programa deberá considerar 2 cuentas bancarias: 1 en soles y
otra en dólares. Considerar el nombre y apellido del titular
- Deberá tener un método para transferir entre sus cuentas, pero
para realizar esto debe hacer una conversión de monedas.
- Otro método para retirar dinero, esto debe actualizar ambas cuentas
y mostrar en pantalla los montos actualizados, a su vez validar si
tiene fondos suficientes o no para el retiro
- Instanciar 3 veces los casos de transferencias para ver reflejado el
uso de tus métodos creados.


"""

class BilleteraE:
    def __init__(self,nombre,apellido,saldo_soles,saldo_dolares):
        self.nombre=nombre
        self.apellido=apellido
        self.saldo_soles=saldo_soles
        self.saldo_dolares=saldo_dolares
        self.tc = 3.77

    def transferencia(self):
        pregunta1 = input("¿Quieres transferir soles o dolares? : ")
        if pregunta1.lower() == 'soles':
            monto = float(input("Ingrese la cantidad de soles a transferir: "))
            if self.saldo_soles >= monto:
                self.saldo_soles = self.saldo_soles - monto
                self.saldo_dolares = self.saldo_dolares + round(monto/self.tc,2)
                print(f"Transferiste {monto} soles a tu cuenta dólares a un TC {self.tc} monto dólares {monto/self.tc:.2f}")
            else:
                print("El saldo de su cuenta soles es insuficiente para realizar la transferencia")
        elif pregunta1.lower() == 'dolares':
            monto = float(input("Ingrese la cantidad de dólares a transferir: "))
            if self.saldo_dolares >= monto:
                self.saldo_dolares = self.saldo_dolares - monto
                self.saldo_soles = self.saldo_soles + round(monto*self.tc,2)
                print(f"Transferiste {monto} soles a tu cuenta dólares a un TC {self.tc} monto dólares {monto / self.tc:.2f}")
            else:
                print("El saldo de su cuenta dólares es insuficiente para realizar la transferencia")

    def retiro(self):
        pregunta2 = input("¿Quieres retirar soles o dolares? : ")
        if pregunta2.lower() == 'soles':
            monto2 = float(input("Ingrese la cantidad de soles a retirar: "))
            if self.saldo_soles >= monto2:
                self.saldo_soles = self.saldo_soles - monto2
                print(f"Retiro {monto2} soles, su saldo actual es de {self.saldo_soles:.2f}")
            else:
                print("Su saldo es insuficiente para realizar el retiro")
        if pregunta2.lower() == 'dolares':
            monto2 = float(input("Ingrese la cantidad de dólares a retirar: "))
            if self.saldo_dolares >= monto2:
                self.saldo_dolares = self.saldo_dolares - monto2
                print(f"Retiro {monto2} soles, su saldo actual es de {self.saldo_dolares:.2f}")
            else:
                print("Su saldo es insuficiente para realizar el retiro")


billetera_electronica = BilleteraE("Joao","Chavez",10000,5000)

billetera_electronica.transferencia()
billetera_electronica.transferencia()
billetera_electronica.transferencia()







