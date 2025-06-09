'''Solicita 10 letras ao usuário, descarta as vogais e retorna em lista as consoantes e total de consoantes'''

from time import sleep

# FUNÇÕES

def verificar_letra():
    lista = []
    for c in range(1, 11):
        while True:           
            pergunta_usuário = input(f"Digite a {c}° letra: ").strip().upper()
            if len(pergunta_usuário) !=1 or not pergunta_usuário.isalpha():
                print("Entrada inválida, digite apenas 1 letra")
            else:
                break    
        if pergunta_usuário in "AEIOU":
            pass
        else:
            lista.append(pergunta_usuário)
    return lista        
            
            
def exibir_resultados(lista):           
    total_consoantes = len(lista)
    print("Analisando...")
    sleep(1)
    print(f"As consoantes identificadas foram: {' - '.join(lista)}")
    sleep(1)
    print(f"Total de consoantes digitadas: {total_consoantes}")
    sleep(1)
    print("Fim do programa. Volte sempre!")


# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    lista= verificar_letra()
    exibir_resultados(lista)
    
     