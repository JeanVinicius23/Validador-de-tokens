import tiktoken

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