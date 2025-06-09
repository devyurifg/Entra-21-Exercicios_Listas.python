'''Solicita nome de 5 usuários, pede sua idade e altura, armazena e retorna no formato de lista'''

#FUNÇÕES

def entrada_usuario():
    lista=[]
    for v in range (1,6):
        while True:
            entrada_nome=input("Qual seu nome: ").strip()
            if entrada_nome.replace(" ", "").isalpha():
                break
            else:
                print("Nome inválido! Digite um nome sem números ou símbolos.")
                
        while True:
            entrada_idade=input("Qual sua idade: ")
            try:
                usuario_idade=int(entrada_idade)
                break
            except:
                print("Entrada inválida! Digite apenas um número válido.")
                
        while True:
            entrada_altura=input("Qual sua altura: ")
            try:
                usuario_altura=float(entrada_altura)
                break
            except:
                print("Entrada inválida! Digite apenas um número válido.")
                    
        lista.append({"Nome": entrada_nome,"Idade":usuario_idade ,"Altura": usuario_altura})
        
    return lista            
                
     
 
        
def exibir_resultados(lista):
    print("\nForam cadastrados os seguintes usuários:\n")
    for i, pessoa in enumerate(lista, start=1):
        print(f"{i}. Nome: {pessoa['Nome']} | Idade: {pessoa['Idade']} | Altura: {pessoa['Altura']} metros")

         
# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    lista= entrada_usuario()
    exibir_resultados(lista)