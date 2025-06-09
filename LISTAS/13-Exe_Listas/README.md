# Classificador de Envolvimento em Crime

Este programa em Python faz cinco perguntas ao usuário relacionadas a um possível envolvimento em um crime. Com base nas respostas fornecidas (sim/não), ele classifica o usuário de acordo com o grau de envolvimento.

## Funcionalidades

- Realiza cinco perguntas relacionadas a um crime:
  - Telefonou para a vítima?
  - Esteve no local do crime?
  - Mora perto da vítima?
  - Devia para a vítima?
  - Já trabalhou com a vítima?
- Aceita apenas respostas "sim" ou "não" (com ou sem acento).
- Conta quantas respostas positivas ("sim") foram fornecidas.
- Classifica o usuário com base no número de respostas "sim":
  - **0 ou 1:** Inocente  
  - **2:** Suspeito  
  - **3 ou 4:** Cúmplice  
  - **5:** Assassino

## Exemplo de Uso
```
Telefonou para a a vítima? (sim/não): sim
Esteve no local do crime? (sim/não): não
Mora perto da vítima? (sim/não): sim
Devia para a vítima? (sim/não): sim
Já trabalhou com a vítima? (sim/não): sim

Respostas registradas:

Telefonou para vitima: sim
Esteve no local do crime: não
Mora perto da vítima: sim
Devia para a vítima: sim
Já trabalhou com a vítima: sim

Total de respostas 'sim': 4

Classificação: Cúmplice
```
## Tecnologias Usadas

- Python 3.x  
- Estrutura `try/except` para validação  
- Estruturas condicionais `if/elif/else`  
- Manipulação de strings (`strip()`, `lower()`)

## Autor

[Yuri Ferreira Gomes](https://github.com/devyurifg)  
📧 devyurifg@gmail.com