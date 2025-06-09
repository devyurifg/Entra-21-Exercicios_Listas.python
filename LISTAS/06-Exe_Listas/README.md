# Sistema de Cadastro e Cálculo de Médias de Alunos

Este programa em Python solicita o nome e as quatro notas de um aluno, calcula a média aritmética e armazena todas as informações em uma estrutura organizada. Ao final, exibe os dados e destaca os alunos com média igual ou superior a 7.

## Funcionalidades

- Solicita o nome do aluno com validação de entrada.
- Solicita quatro notas com validação numérica e de intervalo (0 a 10).
- Calcula a média aritmética das notas.
- Armazena os dados (nome, notas e média) em uma lista de dicionários.
- Exibe um relatório formatado com os dados de cada aluno.
- Destaca os alunos aprovados com média igual ou superior a 7. 

## Exemplo de Uso
```
Digite o nome do 1 aluno: Yuri Ferreira Gomes
Digite a 1° de Yuri Ferreira Gomes: 8.0
Digite a 2° de Yuri Ferreira Gomes: 7.5
Digite a 3° de Yuri Ferreira Gomes: 9.0
Digite a 4° de Yuri Ferreira Gomes: 8.5

------------------- Resultados dos alunos --------------------
1 - Yuri Ferreira Gomes: Notas = [8.0, 7.5, 9.0, 8.5] | Média = 8.25

---------- Alunos aprovados com média maior que 7 -----------
1 - Yuri Ferreira Gomes com média 8.25
```
## Tecnologias Usadas

- Python 3.x  
- Estrutura `try/except` para tratamento de erros de entrada  
- Validação de nome com `isalpha()` e `replace()`  
- Validação de notas entre 0 e 10  
- Formatação de saída com `f-strings` 

## Autor

[Yuri Ferreira Gomes](https://github.com/devyurifg)  
📧 devyurifg@gmail.com