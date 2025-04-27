from controllers.clases import Estudiantes
from models.dao import EstudiantesDAO

dao = EstudiantesDAO()

print("Ingrese los datos del estudiante. Escriba 'salir' para finalizar.")
while True:
    carnet = input("Carnet: ").strip()
    if carnet.lower() == "salir":
        break
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()

    try:
        estatura = float(input("Estatura: ").strip())
        promedio = float(input("Promedio: ").strip())
    except ValueError:
        print("Error: Estatura y promedio deben ser números.")
        continue
    sexo = input("Sexo: ").strip()

    estudiante = Estudiantes(carnet, nombre, apellido, estatura, sexo, promedio)
    dao.estudiantes.append(estudiante)

print("\nCriterios disponibles para ordenar:")
print("1. Carnet")
print("2. Nombre")
print("3. Apellido")
print("4. Estatura")
print("5. Sexo")
print("6. Promedio")
print("7. Salir")

criterios = {
    "1": "carnet",
    "2": "nombre",
    "3": "apellido",
    "4": "estatura",
    "5": "sexo",
    "6": "promedio"
}

while True:
    print("\nIngrese el criterio de ordenamiento (1-6) o 7 para salir:")
    criterio = input().strip()
    if criterio == "7":
        print("Saliendo del programa...")
        break
    if criterio in criterios:
        dao.ordenar_estudiantes(criterios[criterio])
        print(f"\nEstudiantes ordenados por {criterios[criterio]} (ascendente):")
        for estudiante in dao.estudiantes:
            print(estudiante)
    else:
        print("Criterio no válido. Intente nuevamente.")

