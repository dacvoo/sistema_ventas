class FacturaDetalle:
    """ Clase que implementa el detalle de una factura"""
    def __init__(self, item, codigo, nombre,cantidad, precio_unitario) -> None:
        self.item=item
        self.codigo=codigo
        self.nombre=nombre
        self.cantidad=cantidad
        self.precio_unitario=precio_unitario
        self.base_imponible=(cantidad*precio_unitario)/1.18
        self.igv=(cantidad*precio_unitario)-((cantidad*precio_unitario)/1.18)
        self.total=cantidad*precio_unitario
        pass
    def convertir_a_string(self):
        return "|{}|{}|{}|{}|{}|{}|{}|".format(self.item,
                                         self.codigo,
                                         self.nombre,
                                         self.cantidad,
                                         self.precio_unitario,
                                         self.igv,
                                         self.total)