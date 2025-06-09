'''Solicita 10 números inteiros do usuário, armazena-os em uma lista e calcula a soma dos quadrados desses números.'''

# FUNÇÕES

def verificar_números():
    lista=[]
    for c in range(1,11):
        while True:
            entrada_usuario=input(f"Digite seu {c}° número: ")
            try:
                numero_usuario=int(entrada_usuario)
                lista.append(numero_usuario)
                break
            except:
                print("Entrada inválida! Digite apenas um número inteiro.")                
    soma_quadrados = sum(num ** 2 for num in lista)                        
    return lista, soma_quadrados 

def exibir_resultados(lista,soma_quadrados):
    print("Números digitados:", ", ".join(str(num) for num in lista))
    print(f"A soma dos quadrados dos 10 números coletados são {soma_quadrados}") 
    
 
# PROGRAMA PRINCIPAL

if __name__ == "__main__": 
    lista,soma_quadrados =verificar_números()
    exibir_resultados(lista,soma_quadrados)
              