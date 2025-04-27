

class Estudiantes:
    def __init__(self, carnet, nombre, apellido, estatura, sexo, promedio):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.estatura = estatura
        self.sexo = sexo
        self.promedio = promedio

    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}, Carnet: {self.carnet}, Estatura: {self.estatura}, Sexo: {self.sexo}, Promedio: {self.promedio}"
    