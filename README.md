# Calculadora Interativa em Python

## Índice

- [Descrição](#descrição)
- [Como Usar](#como-usar)
- [Exemplo de Saída Esperada](#exemplo-de-saída-esperada)
- [Pré-Requisitos](#pré-requisitos)
- [Contribuições](#contribuições)
- [Licença](#licença)
- [Contatos e Network](#contatos-e-network)


## Descrição

Este projeto contém um código de uma **calculadora interativa** em Python. O objetivo principal é permitir que o usuário realize operações matemáticas básicas de forma simples e interativa diretamente no terminal, com as seguintes funcionalidades:

- **Soma**
- **Subtração**
- **Multiplicação**
- **Divisão** (com tratamento para erro de divisão por zero)

O código apresenta um menu de opções onde o usuário escolhe a operação desejada, insere dois números, e recebe o resultado de imediato. O fluxo continua até que o usuário escolha a opção de sair (`s`). O código também implementa um tratamento de erro para garantir que o usuário insira apenas valores numéricos válidos e escolha opções válidas no menu.

Este projeto foi desenvolvido como parte de um estudo de Python e pode ser útil para iniciantes que desejam entender conceitos de manipulação de entrada/saída, condições, laços de repetição, e tratamento de erros.


## Como Usar

### 1. **Clone o Repositório**
   Para clonar este repositório em seu computador, execute o seguinte comando:
   ```bash
   git clone https://github.com/jacivaldocarvalho/calculadora-interativa-python.git
   ```

### 2. **Instale o Python**
   O código foi desenvolvido utilizando **Python 3.x**. Se você não tem o Python instalado, baixe a versão mais recente [aqui](https://www.python.org/downloads/).

### 3. **Execute o Script**
   Após clonar o repositório e garantir que o Python está instalado, abra o terminal ou prompt de comando e navegue até o diretório do repositório clonado. Em seguida, execute o código com o seguinte comando:
   ```bash
   python calculadora_interativa.py
   ```

   O programa exibirá um menu interativo onde você pode escolher a operação desejada. O cálculo será feito conforme os valores inseridos.

### 4. **Menu de Opções**
   O script irá pedir para que o usuário escolha uma das seguintes operações:
   - **1**: Soma
   - **2**: Subtração
   - **3**: Multiplicação
   - **4**: Divisão
   - **s**: Sair (finaliza a execução)

### 5. **Exemplo de Uso**
   O código solicitará a entrada de dois números após a escolha de uma operação, e retornará o resultado no formato com duas casas decimais. Caso um número inválido seja inserido, o programa pedirá para inserir novamente.


## Exemplo de Saída Esperada

Aqui está um exemplo de como o código funcionará ao ser executado:

```
Bem vindo a minha calculadora!
Escolha uma operação:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
s: Sair
Digite o número para a operação que deseja: 1
Digite o primeiro valor: 10
Digite o segundo valor: 5

O resultado é: 15.00

Bem vindo a minha calculadora!
Escolha uma operação:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
s: Sair
Digite o número para a operação que deseja: 4
Digite o primeiro valor: 10
Digite o segundo valor: 0

O resultado é: Erro: Divisão por zero não é permitida.
```


## Pré-Requisitos

Este código foi desenvolvido utilizando **Python 3.x**. Não há dependências externas, então o único requisito é ter o Python instalado em seu sistema.


## Contribuições

Se você tiver sugestões de melhorias ou encontrar problemas com o código, sinta-se à vontade para abrir um **issue** ou submeter um **pull request**.

## Contatos e Network

- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/jacivaldocarvalho/) 👔
- **E-mail**: [E-mail](mailto:jacivaldocarvalho@gmail.com) 📧
- **GitHub**: [GitHub](https://github.com/jacivaldocarvalho) 🐙
- **Medium**: [Medium](https://medium.com/@jacivaldocarvalho) ✍️

Sempre aberto a novas conexões e oportunidades de aprendizado!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
