class Persona:
    """Clase que construye una persona"""
    def __init__(self, dni="", nombres="", apellidos="", direccion="", telefono="") -> None:
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
    
    def convertir_a_string(self):
        return "|{}|{}|{}|{}|{}|".format(self.dni,
                                         self.nombres,
                                         self.apellidos,
                                         self.direccion,
                                         self.telefono)

        