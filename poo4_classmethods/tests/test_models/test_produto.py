from models import Produto

def test_nao_deve_ter_preco_negativo():
    given = -10
    result = Produto(1, 'guaraná', given, 123)
    expected = 0.01
    
    assert result.preco == expected
    
def test_deve_aceitar_preco_positivo():
    given = 10
    result = Produto(1, 'guaraná', given, 123)
    expected = 10
    
    assert result.preco == expected

def test_deve_aceitar_preco_positivo_para_preco_depois_da_construcao():
    result = Produto(1, 'guaraná', 5, 123)
    
    given = 10
    result.atribui_preco(given)
    expected = 10
    
    assert result.preco == expected