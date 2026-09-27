# Pesquisa de Opinião

Este projeto é um programa em Python que realiza uma pesquisa de opinião com 50 participantes. O sistema coleta:

- nome
- idade
- opinião sobre o atendimento

As respostas podem ser: `Excelente`, `Bom` ou `Ruim`. O programa conta quantas pessoas responderam `Excelente` e quantas responderam `Ruim`, e mostra o total ao final.

## Como executar

1. Certifique-se de que o Python 3 está instalado em sua máquina.
2. Abra o terminal no diretório do projeto.
3. Execute o comando:

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

## Observações

- A opção `Bom` é aceita, mas não altera a contagem final.
- O código foi desenvolvido como uma atividade simples de contagem de opiniões.
