# Pesquisa de Opinião

# Descrição
Este projeto é um programa em Python que realiza uma pesquisa de opinião com 50 participantes. O sistema coleta:

- nome
- idade
- opinião sobre o atendimento

As respostas podem ser: `Excelente`, `Bom` ou `Ruim`. O programa conta quantas pessoas responderam `Excelente` e quantas responderam `Ruim`, e mostra o valor total no final.

## Como executar
1. Ter Python instalado.
2. Abrir o projeto.
3. Execute:

```bash
python app.py
```

4. Digite os dados solicitados para cada participante.

## Exemplo de funcionamento

O programa pede informações como:

```text
Nome: Ana
Idade: 25
Opinião sobre nosso atendimento? ("Excelente", "Bom", "Ruim"): Excelente
```

Ao final, o programa exibe algo semelhante a:

```text
Número de opiniões Excelente: 30  Número de opiniões Ruim: 10
```

## Regras do programa

- `Excelente` → aumenta o contador de avaliações excelentes.
- `Bom` → é aceito, mas não é contabilizado.
- `Ruim` → aumenta o contador de avaliações ruins.
- A pesquisa é realizada com 50 participantes.

## Linguagem/Conceitos utilizados
- ![Python](https://img.shields.io/badge/Python-orange?logo=python)
- `for`
- `if` e `elif`
- `input()`
- Contadores com `+= 1`
- `range()`

## Status

🟢 Concluído

![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)
