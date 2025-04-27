import controllers.clases as c

def main():
    sistema = c.SistemaPacientes()

    while True:
        print("\nMenu de sistema de pacientes: ")
        print("1. Agregar paciente")
        print("2. Mostrar pacientes")
        print("3. Atender paciente")
        print("4. Salir")
        op = input("Ingrese una opción: ").strip()
        if op == "1":
            nombre = input("Ingrese el nombre del paciente: ").strip()
            edad = input("Ingrese la edad del paciente: ").strip()
            sintoma = input("Ingrese el síntoma del paciente: ").strip()
            prioridad = input("Ingrese la prioridad del paciente (de 1 a 5): ").strip()
            sistema.agregar_paciente(nombre, edad, sintoma, prioridad)
        elif op == "2":
            sistema.mostrar_pacientes()
        elif op == "3":
            nombre = input("Ingrese el nombre del paciente a atender: ").strip()
            if sistema.eliminar_paciente(nombre):
                print(f"Paciente {nombre} ha sido atendido.")
            else:
                print(f"Paciente {nombre} no encontrado.")
        elif op == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()