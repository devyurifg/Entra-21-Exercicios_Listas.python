# Identificação de Consoantes

Este é um programa simples em Python que solicita 10 letras ao usuário, descarta as vogais e retorna em uma lista apenas as consoantes digitadas, além de exibir o total de consoantes identificadas, com uma breve simulação de análise.

## Funcionalidades

- Solicita ao usuário que insira 10 letras, uma por uma.
- Valida se a entrada é uma letra única e válida.
- Descarta vogais (A, E, I, O, U).
- Armazena apenas as consoantes em uma lista.
- Exibe as consoantes identificadas e o total de consoantes.
- Simula uma análise usando `sleep()` para uma melhor experiência visual.

## Exemplo de Uso
```
Digite a 1° letra: a
Digite a 2° letra: b
Digite a 3° letra: e
Digite a 4° letra: f
Digite a 5° letra: g
Digite a 6° letra: i
Digite a 7° letra: k
Digite a 8° letra: o
Digite a 9° letra: l
Digite a 10° letra: u
Analisando...
As consoantes identificadas foram: B - F - G - K - L
Total de consoantes digitadas: 5
Fim do programa. Volte sempre!
```
## Tecnologias Usadas

- Python 3.x  
- Módulo `time.sleep` para simular tempo de processamento.  
- Validação de entrada com `isalpha()` e verificação de comprimento da string  

## Autor

[Yuri Ferreira Gomes](https://github.com/devyurifg)  
📧 devyurifg@gmail.com