'''Solicita 4 notas do usuário, calcula a média e retorna lista e média.'''

from time import sleep

# FUNÇÕES

def notas():
    lista=[]
    for c in range (1,5):
        while True:
            entrada=input(f"Digite a {c}° nota: ")
            try:
                usuário_nota = float(entrada)
                lista.append(usuário_nota)
                break  
            except ValueError:
                print("Entrada inválida! Digite um número válido.")
    média=sum(lista)/len(lista)
    return lista, média
    

def exibir_notas(lista,média):    
    print("Calculando...")
    sleep(1) 
    print(f"Notas: {' - '.join(str(nota) for nota in lista)}")
    sleep(1)
    print(f"Média: {média:.2f}")
    sleep(1)
    print("Fim do programa. Volte sempre!")       


# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    lista,média=notas()
    exibir_notas(lista,média)
