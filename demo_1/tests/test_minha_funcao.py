from main import minha_funcao, TESTE


def test_retorna_o_nome():
    given = 'Adilson'
    result = minha_funcao(given)
    expected = 'Adilson'
    
    assert result == expected