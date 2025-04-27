from controllers.clases import Estudiantes

class EstudiantesDAO:
    def __init__(self):
        self.estudiantes = []

    def ordenar_estudiantes(self, parametro):
        self.estudiantes.sort(key=lambda estudiante: getattr(estudiante, parametro))
    