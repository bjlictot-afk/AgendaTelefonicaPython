import datetime

# =========================
# CLASE CONTACTO
# =========================
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


# =========================
# CLASE AGENDA (NUEVA)
# =========================
class Agenda:
    def __init__(self):
        self.contactos = []   # VECTOR
        self.historial = []   # MATRIZ

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("Contacto agregado correctamente.")

    def buscar_contacto(self, nombre):
        encontrado = False
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                c.mostrar()
                encontrado = True

                self.historial.append([
                    "BUSQUEDA",
                    nombre,
                    str(datetime.datetime.now())
                ])

        if not encontrado:
            print("Contacto no encontrado.")

    def mostrar_contactos(self):
        if len(self.contactos) == 0:
            print("No existen contactos registrados.")
        else:
            for c in self.contactos:
                c.mostrar()

    def eliminar_contacto(self, nombre):
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                self.contactos.remove(c)
                print("Contacto eliminado.")

                self.historial.append([
                    "ELIMINADO",
                    nombre,
                    str(datetime.datetime.now())
                ])
                return

        print("Contacto no encontrado.")

    def ver_historial(self):
        if len(self.historial) == 0:
            print("No hay historial registrado.")
        else:
            print("\n====== HISTORIAL (MATRIZ) ======")
            for fila in self.historial:
                print(fila)


# =========================
# PROGRAMA PRINCIPAL
# =========================
agenda = Agenda()

while True:
    print("\n====== AGENDA TELEFÓNICA ======")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Eliminar contacto")
    print("5. Ver historial")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")

        contacto = Contacto(nombre, apellido, telefono, correo, direccion)
        agenda.agregar_contacto(contacto)

    elif opcion == "2":
        nombre = input("Ingrese el nombre a buscar: ")
        agenda.buscar_contacto(nombre)

    elif opcion == "3":
        agenda.mostrar_contactos()

    elif opcion == "4":
        nombre = input("Nombre del contacto a eliminar: ")
        agenda.eliminar_contacto(nombre)

    elif opcion == "5":
        agenda.ver_historial()

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")