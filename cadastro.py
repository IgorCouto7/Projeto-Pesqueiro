class Cliente:
    def __init__(self, nome: str, telefone: str, email: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def editar(self, nome=None, telefone=None, email=None):
        if nome:
            self.nome = nome
        if telefone:
            self.telefone = telefone
        if email:
            self.email = email


class CadastroClientes:
    def __init__(self):
        self.clientes = []

    def adicionar(self, cliente: Cliente):
        self.clientes.append(cliente)

    def excluir(self, email: str):
        self.clientes = [c for c in self.clientes if c.email != email]

    def buscar(self, email: str):
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente
        return None
