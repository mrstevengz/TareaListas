class Paciente:
    def __init__(self, nombre, edad, sintoma, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad
        self.siguiente = None
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sintoma: {self.sintoma}, Prioridad: {self.prioridad}"
    
    
class SistemaPacientes:
    def __init__(self):
        self.inicio = None

    def agregar_paciente(self, nombre, edad, sintoma, prioridad):
        nuevo_paciente = Paciente(nombre, edad, sintoma, prioridad)
        if self.inicio is None:
            self.inicio = nuevo_paciente
        else:
            actual = self.inicio
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_paciente

    def mostrar_pacientes(self):
        pacientes = []
        actual = self.inicio
        while actual is not None:
            print(actual)
            actual = actual.siguiente
        
        pacientes.sort(key=lambda x: x.prioridad)

        for paciente in pacientes:
            print(paciente)

    def eliminar_paciente(self, nombre):
        actual = self.inicio
        anterior = None

        while actual is not None:
            if actual.nombre == nombre:
                if anterior is None:
                    self.inicio = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente

        return False
