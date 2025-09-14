# Delivery System Project

[![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Code Style: ruff](https://img.shields.io/badge/code%20style-ruff-blueviolet?logo=ruff)](https://docs.astral.sh/ruff/)

Um sistema automatizado de pedidos

---

## Sumário

- [Pré-requisitos](#pré-requisitos)
- [Configuração do ambiente virtual (venv)](#configuração-do-ambiente-virtual-venv)
- [Instalação das dependências](#instalação-das-dependências)
- [Code style e lint com ruff](#code-style-e-lint-com-ruff)
- [Pre-commit hooks](#pre-commit-hooks)
- [Formatters e Linters](#formatters-e-linters)
- [Owners do Projeto](#owners-do-projeto)

---

## Pré-requisitos

- Python 3.10 ou superior
- [pip](https://pip.pypa.io/en/stable/)
- [git](https://git-scm.com/)

---

## Configuração do ambiente virtual (venv)

> **Observação:** O `venv` já vem incluso nas versões modernas do Python (3.3+). Não é necessário instalar nada extra no Windows ou Linux, basta ter o Python instalado.

### Windows

No PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Para desativar o ambiente virtual use o comando:

```
deactivate
```

Se aparecer erro de permissão no PowerShell, execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

E tente ativar novamente.

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Instalação das dependências

```bash
pip install -r requirements.txt
```

---

## Pre-commit hooks

Automatize verificações antes de cada commit usando [pre-commit](https://pre-commit.com/):

1. Instale o pre-commit:
   ```bash
   pip install pre-commit
   ```
2. Caso queira instale os hooks definidos no `.pre-commit-config.yaml`:
   ```bash
   pre-commit install
   ```
3. Agora, ao rodar `git commit`, os hooks serão executados automaticamente.

---

## Formatters e Linters

- **Formatters** (ex: `black`, `ruff format`): ajustam automaticamente o formato do código para seguir padrões definidos.
- **Linters** (ex: `ruff`, `flake8`): analisam o código em busca de erros, más práticas e violações de estilo, podendo ou não corrigir automaticamente.

Utilizar ambos garante código limpo, padronizado e com menos bugs.

---

## Owners do Projeto

- [Udson Willams](https://github.com/UdsonWillams/)
- [José Eduardo](https://github.com/Ferreira3)
- [Everton Ribeiro](https://github.com/EvertonDR)
