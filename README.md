# Streamly - Sistema de Locadora de Filmes Online

![Logo](https://github.com/user-attachments/assets/cb15ebe0-7ca3-4ab4-ad75-de9b75fe3cbb)

## Descrição

Streamly é um sistema de locadora de filmes online desenvolvido em Python. O sistema permite listar filmes disponíveis, alugar filmes, devolver filmes e calcular multas por atraso na devolução.

## Funcionalidades

- **Listagem de Filmes**: Exibe todos os filmes disponíveis para locação de forma numerada.
- **Aluguel de Filmes**: Permite ao usuário escolher um filme disponível e definir por quantos dias deseja alugá-lo.
- **Devolução de Filmes**: Permite ao usuário devolver um filme alugado, com cálculo de multa caso haja atraso na devolução.
- **Sistema de Multa**: Cobra R$ 2,00 por dia de atraso na devolução do filme.

## Catálogo de Filmes

Atualmente, o sistema conta com os seguintes filmes:

- Vingadores: Ultimato
- O Poderoso Chefão
- Pulp Fiction
- Matrix
- O Senhor dos Anéis: A Sociedade do Anel
- Star Wars: Episódio V - O Império Contra-Ataca
- Interestelar
- Cidade de Deus
- Jurassic Park
- Titanic
- Invocação do Mal
- Como Treinar seu Dragão
- Godzilla
- F1
- Jurassic World

## Como Executar

Para executar o sistema, basta rodar o arquivo `locadora.py` com o Python:

```python
python locadora.py
```

## Estruturas Utilizadas

O sistema utiliza as seguintes estruturas de programação:

- **Listas**: Para armazenar os filmes disponíveis.
- **Dicionários**: Para armazenar os filmes alugados e seus prazos de devolução.
- **Loop While**: Para manter o sistema em execução até que o usuário escolha sair.
- **Loop For**: Para listar os filmes de forma numerada.
- **Condicionais**: Para verificar opções escolhidas pelo usuário e calcular multas por atraso.
