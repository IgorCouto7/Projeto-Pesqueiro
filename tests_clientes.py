import pytest
from cadastro import Cliente, CadastroClientes

# ==========================
# Testes Positivos
# ==========================

def test_adicionar_cliente_positivo():
    cadastro = CadastroClientes()
    cliente = Cliente("Igor", "123456789", "igor@pesqueiro.com")
    cadastro.adicionar(cliente)
    # Verifica se o cliente foi adicionado
    assert cadastro.buscar("igor@pesqueiro.com") == cliente

def test_editar_cliente_positivo():
    cliente = Cliente("Lucas", "111222333", "lucas@pesqueiro.com")
    cliente.editar(nome="Lucas Silva", telefone="999888777")
    # Verifica se os dados foram atualizados
    assert cliente.nome == "Lucas Silva"
    assert cliente.telefone == "999888777"
    assert cliente.email == "lucas@pesqueiro.com"

def test_excluir_cliente_positivo():
    cadastro = CadastroClientes()
    cliente = Cliente("Ana", "555666777", "ana@pesqueiro.com")
    cadastro.adicionar(cliente)
    cadastro.excluir("ana@pesqueiro.com")
    # Verifica se o cliente foi removido
    assert cadastro.buscar("ana@pesqueiro.com") is None

# ==========================
# Testes Negativos
# ==========================

def test_buscar_cliente_inexistente():
    cadastro = CadastroClientes()
    # Deve retornar None ao buscar cliente que não existe
    assert cadastro.buscar("naoexiste@pesqueiro.com") is None

def test_excluir_cliente_inexistente():
    cadastro = CadastroClientes()
    # Nenhum cliente para excluir, lista deve continuar vazia
    cadastro.excluir("naoexiste@pesqueiro.com")
    assert cadastro.clientes == []

def test_editar_cliente_sem_dados():
    cliente = Cliente("Pedro", "444555666", "pedro@pesqueiro.com")
    # Edita sem passar novos dados
    cliente.editar()
    # Os dados devem continuar os mesmos
    assert cliente.nome == "Pedro"
    assert cliente.telefone == "444555666"
    assert cliente.email == "pedro@pesqueiro.com"
