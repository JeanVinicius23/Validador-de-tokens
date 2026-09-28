from validador import validar_janela_contexto

print("=== Validador de Prompts para LLMs ===")

meu_prompt = input("Escreva o texto que deseja enviar para a IA: ")

print("\nModelos comuns: gpt-3.5-turbo, gpt-4, gpt-4o")
ia_escolhida = input("Qual modelo de IA deseja testar? (Deixe em branco para usar gpt-3.5-turbo): ")

# Se o usuário apenas apertar Enter sem digitar nada, usamos um modelo padrão aqui
if not ia_escolhida.strip():
    ia_escolhida = "gpt-3.5-turbo"

limite_da_ia = 20 # Mantemos um limite baixo para só pra testar

#Executa a validação com os dados que o usuário digitou
status, mensagem = validar_janela_contexto(
    texto=meu_prompt, 
    limite_tokens=limite_da_ia, 
    modelo=ia_escolhida
)

print("\n--- Resultado da Análise ---")
print(f"Modelo avaliado: {ia_escolhida}")
print(mensagem)