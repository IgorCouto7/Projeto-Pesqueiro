import uuid

class Peixe:
    def __init__(self, nome: str, valor: float):
        self.nome = nome # Nome da espécie do peixe.
        self.valor = valor # Valor do kg do peixe em reais.
        self.id = str(uuid.uuid4()) # ID único para cada peixe

    def editar(self, nome=None, valor=None):
        if nome:
            self.nome = nome
        if valor:
            self.valor = valor
    def calcularPreco(self, peso: float):
        if self.valor > 0 and peso > 0:
            return peso * self.valor
        else:
            return None

class CadastroPeixes:
    def __init__(self):
        self.peixes = []

    def adicionar(self, peixe: Peixe):
         self.peixes.append(peixe)

    def excluir(self, id: str):
        self.peixes = [p for p in self.peixes if p.id != id]

    def buscar(self, id: str):
        for peixe in self.peixes:
            if peixe.id == id:
                return peixe
        return None