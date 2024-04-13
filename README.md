# V1 - Sistema Simples de Controle Bancário

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
python .\v1\sistema_bancario.py
```

# V2 - Sistema de Controle Bancário Com POO

Nesta versão avançada do sistema de controle bancário, foi adotado o paradigma de Programação Orientada a Objetos (POO), proporcionando uma estrutura mais organizada e modularizada.

## Funcionalidades

### Menu de Opções

O programa continua a exibir um menu de opções, oferecendo ao usuário as seguintes operações:

 - [1] Depositar
 - [2] Sacar
 - [3] Extrato
 - [4] Nova conta
 - [5] Novo usuário 
 - [6] Listar contas
 - [0] Sair  

### Classes e Encapsulamento

Foram definidas classes para representar os principais conceitos do sistema bancário, como Conta e Movimentação. O encapsulamento foi utilizado para proteger os dados e garantir a integridade das operações.

### Interface

Uma interface gráfica foi implementada para tornar a interação com o sistema mais amigável e intuitiva. Isso permite uma experiência de usuário mais agradável e facilita a compreensão das operações disponíveis.

### Abstração

A utilização de classes e objetos permite uma abstração mais eficiente dos elementos do sistema bancário, simplificando o desenvolvimento e manutenção do código.

### Modularidade e Reutilização

O código foi dividido em módulos que representam as diferentes funcionalidades do sistema, promovendo a reutilização de código e facilitando a manutenção e expansão do sistema no futuro.

### Herança e Polimorfismo

O conceito de herança foi aplicado para estender as funcionalidades das classes, enquanto o polimorfismo permite que diferentes objetos se comportem de maneira específica, dependendo do contexto.

### Tratamento de Exceções

Foram implementados mecanismos de tratamento de exceções para lidar com situações inesperadas durante a execução do programa, garantindo uma experiência robusta e segura para o usuário.

## Requisitos

- Python 3.x

## Execução

Para executar o programa, basta rodar o script principal, garantindo que todas as dependências estejam instaladas:

```bash
python .\sistema_bancario_v2_poo\main.py
```
