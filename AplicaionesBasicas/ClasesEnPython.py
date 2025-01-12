# iniciamos con la creacion de una clase
class Alumno:
    # Constructor de la clase Alumno
    def __init__(self, nombre, nota):
        self.nombre = nombre  # Atributo para almacenar el nombre del alumno
        self.nota = nota  # Atributo para almacenar la nota del alumno

    # Método para mostrar la información del alumno
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}, {self.calcular_resultado()}")
    
    # Método para calcular el resultado del alumno
    def calcular_resultado(self):
        if self.nota >= 5:
            return "Aprobado"
        else:
            return "Suspenso"

# Creamos un objeto de la clase Alumno
alumno1 = Alumno("Juan", 10)

# Llamamos al método mostrar_informacion()
alumno1.mostrar_informacion()

