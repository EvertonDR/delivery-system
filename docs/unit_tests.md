# 🧪 Introdução a Testes em Python

Este documento explica os conceitos básicos de **testes em programação**, com foco em **Python**.

---

## 📍 O que são Testes de Software?

Testes são uma forma de verificar se um programa funciona como deveria.
Em vez de confiar apenas na execução manual, escrevemos **códigos que testam outros códigos**.

### 🔑 Benefícios:

- Detectar erros cedo.
- Garantir que mudanças futuras não quebrem funcionalidades antigas (**regressões**).
- Facilitar a manutenção do sistema.
- Melhorar a qualidade do software.

---

## 🧩 Tipos de Testes

- **Unitários**
  Testam partes isoladas do código (funções, classes).
  Ex.: verificar se uma função de soma retorna o resultado correto.

- **Integração**
  Verificam se diferentes partes do sistema funcionam bem juntas.
  Ex.: comunicação entre módulos de cadastro e banco de dados.

- **Sistema**
  Avaliam a aplicação como um todo, de ponta a ponta.
  Ex.: simular o fluxo de um usuário em um sistema web.

- **Aceitação**
  Validam se o sistema atende aos requisitos do cliente.
  Ex.: “o sistema deve permitir cadastrar um cliente com nome e email”.

No código fornecido, temos **testes unitários**.

---

## ⚡ O que é Pytest?

[pytest](https://docs.pytest.org/) é uma das bibliotecas mais usadas para testes em Python.

### ✨ Vantagens:

- Fácil de começar: qualquer função que comece com `test_` é reconhecida como teste.
- Mensagens de erro claras.
- Integração com `mock` (para simular entradas e saídas).
- Suporte a fixtures, parametrização e plugins.

### ▶️ Como rodar:

```bash
pytest
```
