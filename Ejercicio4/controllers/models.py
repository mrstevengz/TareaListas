class Accion:
    def __init__(self, accion):
        self.accion = accion
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"Accion: {self.accion}"


class Historial:
    def __init__(self):
        self.actual = None
        self.inicio = None
        self.fin = None

    def agregar_accion(self, accion):
        nuevo_accion = Accion(accion)
        if self.inicio is None:
            self.inicio = nuevo_accion
            self.fin = nuevo_accion
        else:
            self.fin.siguiente = nuevo_accion
            nuevo_accion.anterior = self.fin
            self.fin = nuevo_accion
        self.actual = nuevo_accion

    def deshacer(self):
        if self.actual is None or self.actual.anterior is None:
            print("No hay acciones para deshacer.")
            return None
        self.actual = self.actual.anterior
        return self.actual.accion

    def rehacer(self):
        if self.actual is None or self.actual.siguiente is None:
            print("No hay acciones para rehacer.")
            return None
        self.actual = self.actual.siguiente
        return self.actual.accion

    def mostrar_historial(self):
        actual = self.inicio
        if actual is None:
            print("No hay acciones en el historial.")
            return
        while actual is not None:
            print(actual)
            actual = actual.siguiente