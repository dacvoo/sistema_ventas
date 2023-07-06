class Producto:
    """ Clase que implementa producto"""
    def __init__(self, codigo, nombre, precio) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        pass
    def convertir_a_string(self):
        return "|{}|{}|{}|".format(self.codigo,
                                         self.nombre,
                                         self.precio)
