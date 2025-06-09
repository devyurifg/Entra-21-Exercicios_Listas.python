'''Solicita ao usuário 4 números inteiros, validando a entrada, armazena em uma lista 
    contendo os 4 números inteiros digitados pelo usuário..'''

from time import sleep
from math import prod

# FUNÇÕES

def verificar_numeros():
    lista = []
    for c in range(1, 5):
        while True:
            entrada = input(f"Digite o {c}° número inteiro: ")
            try:
                usuario_pergunta = int(entrada)
                lista.append(usuario_pergunta)
                break 
            except ValueError:
                print("Entrada inválida! Digite apenas um número inteiro.")
    return lista


def exibir_resultados(lista):
    '''Exibe os números digitados, sua soma e sua multiplicação.'''        
    print("Analisando...")
    sleep(1)    
    print(f"Você digitou os seguintes números: {' - '.join(str(número) for número in lista)}")
    sleep(1)
    print(f"A soma dos números é: {sum(lista)}")
    sleep(1)
    print(f"A multiplicação dos números é: {prod(lista)}")
    sleep(1)
    print("Fim do programa. Volte sempre!")                   
                    

# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    lista=verificar_numeros()
    exibir_resultados(lista)