# Importamos as duas funções do nosso arquivo validador.py
from validador import conta_tokens, validar_janela_contexto

def test_conta_tokens_texto_vazio():
    #chama a função passando um texto vazio
    resultado = conta_tokens("")
    
    # O assert verifica se o resultado é exatamente 0. 
    # Se for, o teste passa (Fica verde). Se não, falha (Fica vermelho).
    assert resultado == 0

def test_validar_janela_com_sucesso():
    texto = "Olá, IA, me ajude com um teste."
    
    # Passa um texto curto e um limite alto (50 tokens)
    # A função vai devolver duas coisas: um status (True/False) e uma mensagem
    status, mensagem = validar_janela_contexto(texto, limite_tokens=50)
    
    #status devolvido é True (Sucesso)
    assert status == True
    #palavra "Sucesso" está dentro da mensagem devolvida
    assert "Sucesso" in mensagem

def test_validar_janela_com_falha():
    texto = "Este é um texto muito longo que vai forçar um erro na janela de contexto."
    
    # Passando um texto médio, passa o limite para apenas 3 tokens
    status, mensagem = validar_janela_contexto(texto, limite_tokens=3)
    
    # Como o texto tem mais de 3 tokens, o status tem que ser False (Falha)
    assert status == False
    assert "Falha" in mensagem