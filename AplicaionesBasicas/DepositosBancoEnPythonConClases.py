# EJEMPLO BANCO
# creamos la clase banco

class Banco:
    #inicializamos
    def __init__(self):
        self.cliente1 = Cliente("Ivan")
        self.cliente2 = Cliente("Lucía")
        self.cliente3 = Cliente("Nadia")

    # funcion para operar
    def operacion(self):
        self.cliente1.depositar(300)
        self.cliente2.depositar(500)
        self.cliente3.depositar(1000)
        self.cliente1.extraer(200)

    # funcion para obtener los depositos totales
    def depositos(self):
        total = self.cliente1.devolver_cantidad() + self.cliente2.devolver_cantidad() + self.cliente3.devolver_cantidad()
        print("El total de dinero del banco es: ", total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

# creamos la clase Cliente
class Cliente:
    # inicializamos
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    # funcion para depositar dinero
    def depositar(self, cantidad):
        self.cantidad += cantidad

    # fucnion para extraer dinero
    def extraer(self, cantidad):
        self.cantidad -= cantidad

    #funcion para obtener el total de dinero
    def devolver_cantidad(self):
        return self.cantidad
    # funcion para imprimir los datos del cliente
    def imprimir(self):
        print(self.nombre, "tiene depositada una cantidad de ", self.cantidad)

# bloque principal
banco1 = Banco()
banco1.operacion()
banco1.depositos()
