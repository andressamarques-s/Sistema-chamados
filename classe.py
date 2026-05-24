class Chamado:
    def __init__(self, usuario, problema, status):
        self.usuario = usuario
        self.problema = problema
        self.status = status

    def exibir(self):
        return f"{self.usuario} | {self.problema} | {self.status}"

    def esta_aberto(self):
        return self.status == "aberto"


class ChamadoUrgente(Chamado):
    def __init__(self, usuario, problema, status):
        super().__init__(usuario, problema, status)
        self.prioridade = "alta"

    def exibir(self):
        return f"[URGENTE] {self.usuario} | {self.problema} | {self.status}"


class ChamadoAgendado(Chamado):
    def __init__(self, usuario, problema, status, data):
        super().__init__(usuario, problema, status)
        self.data = data

    def exibir(self):
        return f"{self.usuario} | {self.problema} | {self.status} | Agendado para: {self.data}"
