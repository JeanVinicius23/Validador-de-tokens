import tiktoken

# 1. Primeira função: Apenas conta os tokens
def conta_tokens(texto: str, modelo: str = "gpt-3.5-turbo") -> int:
    # Se o utilizador enviar um texto vazio, devolvemos 0 tokens
    if not texto.strip():
        return 0    
    
    # Preparamos a "régua" de medição específica do modelo de IA
    codificador = tiktoken.encoding_for_model(modelo)
    # A função encode corta o texto em pedaços e devolve uma lista
    tokens = codificador.encode(texto)
    # A função len() conta quantos itens existem nessa lista
    return len(tokens)

# 2. Segunda função: Usa a contagem para aprovar ou bloquear o texto
def validar_janela_contexto(texto: str, limite_tokens: int, modelo: str = "gpt-3.5-turbo"):
    # Chamamos a função de cima para saber o tamanho do texto
    qtd_tokens = conta_tokens(texto, modelo)
    
    # Lógica de Teste: Se os tokens forem maiores que o limite, falha.
    if qtd_tokens > limite_tokens:
        return False, f"Falha: O texto possui {qtd_tokens} tokens. O limite é {limite_tokens}."
    
    # Caso contrário, passa no teste.
    return True, f"Sucesso: O texto possui {qtd_tokens} tokens e está dentro do limite."