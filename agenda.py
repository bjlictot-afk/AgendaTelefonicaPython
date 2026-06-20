import datetime


class Contacto:
    def __init__(self, nombre, apellido, telefono, correo, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def mostrar(self):
        print("\n----------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")
        print(f"Dirección: {self.direccion}")
        print("----------------------")


# VECTOR (lista)
contactos = []

# MATRIZ (historial)
historial = []


while True:
    print("\n====== AGENDA TELEFÓNICA ======")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Eliminar contacto")
    print("5. Ver historial (Matriz)")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    # 1. AGREGAR
    if opcion == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")

        contactos.append(Contacto(nombre, apellido, telefono, correo, direccion))

        print("Contacto agregado correctamente.")

    # 2. BUSCAR
    elif opcion == "2":
        buscar = input("Ingrese el nombre a buscar: ")
        encontrado = False

        for contacto in contactos:
            if contacto.nombre.lower() == buscar.lower():
                contacto.mostrar()
                encontrado = True

                historial.append([
                    "BUSQUEDA",
                    buscar,
                    str(datetime.datetime.now())
                ])

        if not encontrado:
            print("Contacto no encontrado.")

    # 3. MOSTRAR
    elif opcion == "3":
        if len(contactos) == 0:
            print("No existen contactos registrados.")
        else:
            for contacto in contactos:
                contacto.mostrar()

    # 4. ELIMINAR
    elif opcion == "4":
        nombre = input("Nombre del contacto a eliminar: ")

        for contacto in contactos:
            if contacto.nombre.lower() == nombre.lower():
                contactos.remove(contacto)
                print("Contacto eliminado.")

                historial.append([
                    "ELIMINADO",
                    nombre,
                    str(datetime.datetime.now())
                ])
                break
        else:
            print("Contacto no encontrado.")

    # 5. MATRIZ (HISTORIAL)
    elif opcion == "5":
        if len(historial) == 0:
            print("No hay historial registrado.")
        else:
            print("\n====== HISTORIAL (MATRIZ) ======")
            for fila in historial:
                print(fila)

    # 6. SALIR
    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")