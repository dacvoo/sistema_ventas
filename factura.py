from persona import Persona
from factura_detalle import FacturaDetalle
class Factura:
    """ Clase que implementa la factura """
    def __init__(self, numero, cliente:Persona, total, detalle) -> None:

        self.serie='F002'
        self.numero=numero
        self.cliente:Persona=cliente
        self.base_imponible=total/1.18
        self.igv=total-(total/1.18)
        self.detalle:list=detalle
        self.total=total
        pass
    def convertir_a_string(self):
        return "|{}|{}|{}|{}|{}|{}|".format(self.serie,
                                         self.numero,
                                         self.cliente.nombres,
                                         self.base_imponible,
                                         self.igv,
                                         self.total)