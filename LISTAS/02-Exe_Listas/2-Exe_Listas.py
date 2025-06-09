'''Solicita 10 números reais do usuário e retorna uma lista de forma decrescente ao que ele digitou.'''

from time import sleep

# FUNÇÕES

def verificar_numero():
    lista=[]
    for c in range(1,11):
        while True:            
            entrada=input(f"Digite o {c}° número real: ")
            try:
                usuario_numero=float(entrada)
                lista.append(usuario_numero)
                break
            except ValueError:
                print("Entrada inválida! Digite apenas um número real.")   
    return lista


def exibir_resultados(lista):        
    print("Analisando...")
    sleep(1)    
    print(f"Você digitou os seguintes números: {' - '.join(str(número) for número in lista[::-1])}")
    sleep(1)
    print("Fim do programa. Volte sempre!")    


# PROGRAMA PRINCIPAL 

if __name__ == "__main__":
    lista=verificar_numero()
    exibir_resultados(lista)
