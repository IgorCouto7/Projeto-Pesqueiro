import pytest

from peixe import Peixe, CadastroPeixes

def test_adicionar_peixe():
    cadastro = CadastroPeixes()
    peixe = Peixe("Tilápia", 10.0)
    cadastro.adicionar(peixe)
    # Busca o peixe cadastrado.
    assert cadastro.buscar(peixe.id) == peixe

def test_editar_peixe_typemismatch():
    peixe = Peixe("Bagre", 13.4)
    peixe.editar(nome="Peixe-gato", valor=13.5)
    # Verifica se os dados foram atualizados era pra dar errado
    assert peixe.nome == "Peixe-gato"
    assert peixe.valor == "13.5"

def test_calcularValor_negativevalue():
    peixe = Peixe("Bagre", 13.4)
    preco = peixe.calcularPreco(-1.0)

    # Verifica se o valor foi corretamente filtrado para none para evitar valores negativos
    assert preco is None