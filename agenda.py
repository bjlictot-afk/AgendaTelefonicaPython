class Contacto:
    def __init__(self, nombre, apellido, telefono, correo, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")
        print(f"Dirección: {self.direccion}")
        print("-" * 30)

contactos = []

while True:
    print("\nAGENDA TELEFÓNICA")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")

        contactos.append(
            Contacto(nombre, apellido, telefono, correo, direccion)
        )

        print("Contacto agregado correctamente.")

    elif opcion == "2":
        buscar = input("Ingrese el nombre a buscar: ")

        encontrado = False

        for contacto in contactos:
            if contacto.nombre.lower() == buscar.lower():
                contacto.mostrar()
                encontrado = True

        if not encontrado:
            print("Contacto no encontrado.")

    elif opcion == "3":
        if len(contactos) == 0:
            print("No existen contactos registrados.")
        else:
            for contacto in contactos:
                contacto.mostrar()

    elif opcion == "4":
        nombre = input("Nombre del contacto a eliminar: ")

        for contacto in contactos:
            if contacto.nombre.lower() == nombre.lower():
                contactos.remove(contacto)
                print("Contacto eliminado.")
                break
        else:
            print("Contacto no encontrado.")

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")