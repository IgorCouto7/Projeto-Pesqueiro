import pytest

from peixe import Peixe, CadastroPeixes

def test_adicionar_peixe():
    # Cria um peixe e cadastro mockado
    cadastro = CadastroPeixes()
    peixe = Peixe("Sardinha", 4)

    #Adiciona o Peixe no Cadastro
    cadastro.adicionar(peixe)

    #Testa se foi adicionado
    assert cadastro.buscar(peixe.id) == peixe

def test_editar_peixe():
    peixe = Peixe("Bagre", 13.4)
    peixe.editar(nome="Peixe-gato",valor=13.5)
    # Verifica se ambos os campos foram alterados
    assert peixe.nome == "Peixe-gato" and peixe.valor == 13.5

def test_editar_peixe_valor():
    peixe = Peixe("Bagre", 13.4)
    peixe.editar(valor=13.5)
    # Verifica se apenas o valor foi alterado
    assert peixe.nome == "Bagre" and peixe.valor == 13.5

def test_editar_peixe_nome():
    peixe = Peixe("Bagre", 13.4)
    peixe.editar(nome="Peixe-gato")
    # Verifica se apenas o nome foi alterado
    assert peixe.nome == "Peixe-gato" and peixe.valor == 13.4


def test_excluir_peixe():
    cadastro = CadastroPeixes()
    peixe = Peixe("Tilapia", 14)
    cadastro.adicionar(peixe)
    cadastro.excluir(peixe.id)
    assert cadastro.buscar(peixe.id) is None

def test_excluir_peixe_inexistente():
    cadastro = CadastroPeixes()
    peixe = Peixe("Tilapia", 14)
    cadastro.adicionar(peixe)
    cadastro.excluir("peixe.id inexistente")
    assert cadastro.buscar("peixe.id inexistente") is None

def test_buscar_peixe_inexistente():
    cadastro = CadastroPeixes()
    peixe = Peixe("Barracuda", 18)

    #Adicionando peixe para busca
    cadastro.adicionar(peixe)

    #Testando uma busca por um ID inexistente
    assert cadastro.buscar("peixe.id inexistente") == None

def test_calcularValor():
    peixe = Peixe("Megalodonte", 9999)
    preco = peixe.calcularPreco(1000)

    # Verifica resultado comparando ao esperado
    assert preco == 9999000

def test_calcularValor_negativeweight():
    peixe = Peixe("Bagre", 13.4)
    preco = peixe.calcularPreco(-1.0)

    # Verifica se o valor foi corretamente filtrado para none para evitar valores negativos
    assert preco is None

def  test_calcularValor_negativevalue():
    peixe = Peixe("Bagre", -1.0)
    preco = peixe.calcularPreco(10)

    # Verifica se o valor foi corretamente filtrado para none para evitar valores negativos
    assert preco is None