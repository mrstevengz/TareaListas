import controllers.clases as c

ruta = c.Ruta()

print("Ingrese los datos de las estaciones. Escriba 'salir' para finalizar.")

ruta.agregar_estacion("A", 15)
ruta.agregar_estacion("B", 25)
ruta.agregar_estacion("C", 50)

print("Ruta de la estacion:")
ruta.mostrar_ruta()

print("Tiempo de ruta de A a C:", ruta.calcular_tiempo("A", "C"))
print("Tiempo de ruta de A a B:", ruta.calcular_tiempo("A", "B"))
print("Tiempo de ruta de B a C:", ruta.calcular_tiempo("B", "C"))
print("Tiempo de ruta de C a A:", ruta.calcular_tiempo("C", "A"))