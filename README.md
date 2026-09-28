# 🛡️ Validador de Tokens e Janela de Contexto para LLMs

Uma ferramenta leve e eficiente em Python desenvolvida para calcular tokens, validar limites de contexto e otimizar chamadas a modelos de Inteligência Artificial (como o ecossistema OpenAI/ChatGPT).

## 🚀 O Problema Resolvido
Ao desenvolver aplicações com Grandes Modelos de Linguagem (LLMs), enviar textos que excedem a janela de contexto suportada causa erros na aplicação. Além disso, os custos de API são cobrados por **token**. Este projeto atua como uma camada de segurança (*guardrail*), validando e bloqueando prompts antes que eles cheguem à IA, evitando falhas de sistema e gastos desnecessários.

---

## 📂 Estrutura do Projeto

O projeto segue o princípio de **Separação de Preocupações**, garantindo código limpo, modular e de fácil manutenção:

* 🧠 **`validador.py`**: O motor da aplicação. Contém as funções lógicas de cálculo de tokens (`tiktoken`) e validação de regras de negócio.
* 🧪 **`test_validador.py`**: A suite de testes automatizados construída com `pytest`, garantindo a robustez do código.
* 🖥️ **`main.py`**: A interface de linha de comandos interativa (CLI) para teste dinâmico pelo utilizador final.

---

## ⚙️ Pré-requisitos e Instalação

Certifique-se de ter o **Python** instalado no seu computador. Em seguida, siga os passos abaixo no seu terminal:

1. **Abra o terminal na pasta do seu projeto.**

2. **Crie e ative um ambiente virtual (`venv`):**
   * **No Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * **No Mac/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências necessárias (`tiktoken` e `pytest`):**
   ```bash
   pip install tiktoken pytest

## 🕹️ Como Executar

1. Executar a Interface Interativa (main.py):
   Para testar prompts personalizados em tempo real e escolher diferentes modelos de IA (como gpt-3.5-turbo, gpt-4, gpt-4o):
   python main.py

2. Executar os Testes Automatizados (pytest):
   Para validar se a lógica do código está a funcionar perfeitamente sem erros:
   pytest -v

---

## 🛠️ Tecnologias Utilizadas
* Python (Linguagem principal)
* Tiktoken (Biblioteca de tokenização oficial da OpenAI baseada em BPE)
* Pytest (Framework de testes unitários e automação de QA)

---

## 👨‍💻 Autor

**Jean Vinicius Silva da Silva**
- GitHub:(https://github.com/JeanVinicius23)
  
Desenvolvido com foco em boas práticas de engenharia de software, automação de testes e integração com Inteligência Artificial.
