'''
   - Solicita ao usuário que digite 20 números inteiros, armazenando-os em uma lista geral.
   - Separa esses números em listas de pares e ímpares.
'''

from time import sleep

# FUNÇÕES

def verificar_numeros():
    lista=[]
    lista_par=[]
    lista_impar=[]
    for c in range(1,21):
        while True:
            entrada=(input(f"Digite {c}° número inteiro: "))
            try:
                usuario_numero=int(entrada)
                lista.append(usuario_numero)
                break
            except ValueError:
                print("Entrada inválida! digite apenas um número inteiro")
        if usuario_numero % 2 == 0:
            lista_par.append(usuario_numero)
        else:
            lista_impar.append(usuario_numero)
    return lista, lista_impar, lista_par            


def exibir_resultados(lista, lista_impar, lista_par ):
    print("Analisando...")
    sleep(1)
    print(f"Os números que você digitou foram: {' - '.join(str(num) for num in lista)}")
    sleep(1)
    print(f"Os números pares foram: {' - '.join(str(num) for num in lista_par)} total de {len(lista_par)} números pares")
    sleep(1)
    print(f"Os números ímpares foram: {' - '.join(str(num) for num in lista_impar)} total de {len(lista_impar)} números ímpares")


# PROGRAMA PRINCIPAL


if __name__ == "__main__":   
    lista, lista_impar, lista_par= verificar_numeros()
    exibir_resultados(lista, lista_impar, lista_par)