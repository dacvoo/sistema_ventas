class Cuentas:
    
    def __init__(self, user_name="", contraseña="") -> None:
        self.user_name = user_name
        self.contraseña = contraseña
        
    def convertir_a_string(self):
        return "|{}|{}|".format(self.user_name,self.contraseña)
        