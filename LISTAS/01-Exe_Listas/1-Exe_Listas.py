'''Solicita 5 números inteiros do usuário e retorna uma lista'''

from time import sleep

# FUNÇÕES

def verificar_número():
    lista=[]
    for c in range(1,6):
        usuário_número=int(input(f"Digite o {c}° número inteiro: "))
        lista.append(usuário_número)
    return lista


def exibir_resultados(lista):        
    print("Analisando...")
    sleep(1)    
    print(f"Você digitou os seguintes números: {' - '.join(str(número) for número in lista)}")
    sleep(1)
    print("Fim do programa. Volte sempre!")    


# PROGRAMA PRINCIPAL 

if __name__ == "__main__":
    tomate=verificar_número()
    exibir_resultados(tomate)



