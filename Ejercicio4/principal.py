import controllers.models as c

def main():
    historial = c.Historial()
    while True:
        print("\nMenu de acciones: ")
        print("1. Agregar acción")
        print("2. Deshacer acción")
        print("3. Rehacer acción")
        print("4. Mostrar historial")
        print("5. Salir")
        op = input("Ingrese una opción: ").strip()
        if op == "1":
            print("1. Escribir")
            print("2. Borrar")
            print("3. Pegar")
            print("4. Copiar")
            accion = input("\nIngrese la acción: ").strip()
            if accion == "1":
                accion = "Escribir"
            elif accion == "2":
                accion = "Borrar"
            elif accion == "3": 
                accion = "Pegar"
            elif accion == "4":
                accion = "Copiar"
            else:
                print("Opción inválida. Intente nuevamente.")
                continue
            historial.agregar_accion(accion)
            print(f"Acción '{accion}' agregada al historial.")
        elif op == "2":
            accion = historial.deshacer()
            if accion:
                print(f"Acción deshecha: {accion}")
        elif op == "3":
            accion = historial.rehacer()
            if accion:
                print(f"Acción rehecha: {accion}")
        elif op == "4":
            historial.mostrar_historial()
        elif op == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()