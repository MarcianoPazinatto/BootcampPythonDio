# Sistema Simples de Controle Bancário

Este é um sistema simples de controle bancário implementado em Python. Ele permite que o usuário faça operações básicas como depositar, sacar, exibir o extrato e sair.

## Funcionalidades

### Menu de Opções

O programa exibe um menu de opções que permite ao usuário escolher entre as seguintes operações:

- [d] Depositar
- [s] Sacar
- [e] Extrato
- [q] Sair

### Depositar

Ao selecionar a opção de depósito, o usuário pode inserir o valor que deseja depositar. O sistema verifica se o valor é válido e o adiciona ao saldo atual.

### Sacar

Na opção de saque, o usuário pode inserir o valor que deseja sacar. O sistema verifica se o saldo é suficiente, se o valor excede o limite de saque e se o número máximo de saques foi atingido antes de realizar a operação.

### Extrato

O usuário pode escolher a opção de extrato para exibir todas as movimentações feitas até o momento, incluindo depósitos e saques, bem como o saldo atual.

### Sair

Ao selecionar esta opção, o programa encerra a execução.

## Requisitos

- Python 3.x

## Execução

Para executar o programa, basta executar o script Python `sistema_bancario.py`. Certifique-se de ter Python 3.x instalado em seu sistema.

```bash
python sistema_bancario.py
