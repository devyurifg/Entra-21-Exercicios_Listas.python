'''Solicita ao usuário que digite dois conjuntos de 10 números inteiros cada, armazenando-os em duas listas 
separadas. Em seguida, gera uma terceira lista com os elementos intercalados das duas listas fornecidas.'''

from time import sleep

# FUNÇÕES

def verificar_numeros():
    lista_1=[]
    for c in range (1,11):
        while True:
            entrada_1=input(f"Digite o {c}° número: ")
            try:
                usuario_numero=int(entrada_1)
                lista_1.append(usuario_numero)
                break
            except ValueError:
                print("Entrada inválida! digite apenas um número inteiro")
    print("Armazenando...")
    sleep(1)
    print("Digite mais 10 números")
    sleep(1)
    print("Armazenando...")
    lista_2=[]
    for v in range (1,11):
        while True:
            entrada_2=input(f"Digite o {v}° número: ")
            try:
                usuario_numero=int(entrada_2)
                lista_2.append(usuario_numero)
                break
            except ValueError:
                print("Entrada inválida! digite apenas um número inteiro")
    
    lista_intercalada = []
    for i in range(10):
        lista_intercalada.append(lista_1[i])
        lista_intercalada.append(lista_2[i])            
                    
    return lista_1,lista_2,lista_intercalada            
                        
 
def exibir_resultados(lista_1,lista_2,lista_intercalada):
    print("10 primeiros Números digitados:", ", ".join(str(num) for num in lista_1))
    print("10 ultimos Números digitados:", ", ".join(str(num) for num in lista_2))
    print("Seus números intercalados:", ", ".join(str(num) for num in lista_intercalada))
    
                
#PROGRAMA PRINCIPAL

if __name__ == "__main__":
    lista_1,lista_2,lista_intercalada=verificar_numeros()
    exibir_resultados(lista_1,lista_2,lista_intercalada)            