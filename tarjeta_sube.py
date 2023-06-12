class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

PRECIO_TICKET = 70
DESACTIVADO = 'desactivado'
ACTIVADO = 'activado'
PRIMARIO = 'primario'
SECUNDARIO = 'secundario'
UNIVERSITARIO = 'universitario'
JUBILADO = 'jubilado'


DESCUENTOS = {
    PRIMARIO: 50,
    SECUNDARIO: 40,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}

class Sube():
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO
    
    def obtener_precio_ticket(self):
        # if self.grupo_beneficiario == PRIMARIO:
        #     self.precio_ticket = PRECIO_TICKET/2
        # else:
        #     self.precio_ticket = PRECIO_TICKET
        # return self.precio_ticket
        if self.grupo_beneficiario in DESCUENTOS:
            desc = DESCUENTOS[self.grupo_beneficiario]
            return PRECIO_TICKET * (100 - desc) / 100
        else:
            return PRECIO_TICKET


    def pagar_pasaje(self):
        if self.saldo < self.obtener_precio_ticket():
            raise NoHaySaldoException()
        
        # if self.grupo_beneficiario == PRIMARIO:
        #     self.saldo -= 35
        # else:
        #     self.saldo = self.saldo - 70
        self.saldo = self.saldo - self.obtener_precio_ticket()

        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()

    def cambiar_estado(self,estado = None):
        self.estado = estado

        if self.estado == 'pendiente':
            raise EstadoNoExistenteException()
