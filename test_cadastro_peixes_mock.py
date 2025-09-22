import pytest
from unittest.mock import MagicMock

# Importe as classes do seu arquivo peixe.py
from peixe import Peixe, CadastroPeixes

def test_adicionar_peixe_com_mock():
    """
    Testa se o método 'adicionar' está corretamente inserindo um objeto na lista.
    """
    # Preparação (Arrange)
    cadastro = CadastroPeixes()
    # Criamos um objeto falso que se parece com um Peixe
    peixe_mock = MagicMock(spec=Peixe)

    # Ação (Act)
    cadastro.adicionar(peixe_mock)

    # Verificação (Assert)
    # Verificamos se o objeto falso foi realmente adicionado à lista interna
    assert peixe_mock in cadastro.peixes

def test_buscar_peixe_com_mock_sucesso():
    """
    Testa se o método 'buscar' encontra e retorna o objeto correto.
    """
    # Preparação
    cadastro = CadastroPeixes()
    peixe_mock = MagicMock(spec=Peixe)
    peixe_mock.id = "id-do-peixe-mock" # O método 'buscar' precisa deste atributo

    # Adicionamos o mock diretamente na lista para o teste
    cadastro.peixes.append(peixe_mock)

    # Ação
    resultado = cadastro.buscar("id-do-peixe-mock")

    # Verificação
    # Garante que o objeto encontrado é o nosso mock
    assert resultado == peixe_mock

def test_buscar_peixe_com_mock_nao_encontrado():
    """
    Testa se 'buscar' retorna None quando o ID não existe.
    """
    # Preparação
    cadastro = CadastroPeixes()
    # Não adicionamos nenhum peixe

    # Ação
    resultado = cadastro.buscar("id-inexistente")

    # Verificação
    assert resultado is None

def test_excluir_peixe_com_mock():
    """
    Testa se o método 'excluir' remove o objeto correto da lista.
    """
    # Preparação
    cadastro = CadastroPeixes()
    
    # Criamos dois mocks para garantir que o correto seja excluído
    peixe_mock_a_excluir = MagicMock(spec=Peixe)
    peixe_mock_a_excluir.id = "id-para-excluir"

    peixe_mock_a_manter = MagicMock(spec=Peixe)
    peixe_mock_a_manter.id = "id-para-manter"

    cadastro.peixes = [peixe_mock_a_excluir, peixe_mock_a_manter]

    # Ação
    cadastro.excluir("id-para-excluir")

    # Verificação
    assert len(cadastro.peixes) == 1
    assert peixe_mock_a_excluir not in cadastro.peixes
    assert peixe_mock_a_manter in cadastro.peixes