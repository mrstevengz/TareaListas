class Estacion:
    def __init__(self, nombre, tiemporuta):
        self.nombre = nombre
        self.tiemporuta = tiemporuta
        self.siguiente = None
    
    def __str__(self):
        return f"Estacion: {self.nombre}, Tiempo de ruta: {self.tiemporuta}"
    
class Ruta:
    def __init__(self):
        self.inicio = None

    def agregar_estacion(self, nombre, tiemporuta):
        nueva_estacion = Estacion(nombre, tiemporuta)
        if self.inicio is None:
            self.inicio = nueva_estacion
        else:
            actual = self.inicio
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nueva_estacion
    
    def calcular_tiempo(self, origen, destino):
        actual = self.inicio
        tiempo = 0
        encontrado = False

        while actual is not None:
            if actual.nombre == origen:
                encontrado = True
            if encontrado:
                tiempo += actual.tiemporuta
                if actual.nombre == destino:
                    break

            actual = actual.siguiente

        return None
    
    def mostrar_ruta(self):
        actual = self.inicio
        while actual is not None:
            print(actual)
            actual = actual.siguiente