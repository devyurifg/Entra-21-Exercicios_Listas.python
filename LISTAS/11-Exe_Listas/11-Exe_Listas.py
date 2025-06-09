'''Solicita nome de 5 alunos, pede sua idade e altura, armazena e retorna no formato de lista'''

#FUNÇÕES

def entrada_usuario():
    lista=[]
    for v in range (1,6):
        while True:
            entrada_nome=input("Qual nome do aluno: ").strip()
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
    print("\nForam cadastrados os seguintes alunos:\n")
    for i, pessoa in enumerate(lista, start=1):
        print(f"{i}. Nome: {pessoa['Nome']} | Idade: {pessoa['Idade']} | Altura: {pessoa['Altura']} metros")
        
def analise_de_dados(lista):
    '''Faz a análise dos alunos com mais de 13 anos e calcula:A média da altura desses alunos, Quantos estão abaixo da média de altura'''
    print("\nSeguintes alunos tem mais de 13 anos:\n")
    alunos_mais_13=[p for p in lista if p['Idade'] > 13]
    if not alunos_mais_13:
        print("Não há alunos com mais de 13 anos na lista.")
        return 0
    for aluno in alunos_mais_13:
        print(f"Nome: {aluno['Nome']} | Idade: {aluno['Idade']} | Altura: {aluno['Altura']} metros")
    
    print("\nMédia da altura dos alunos com mais de 13 anos na lista:\n")
    media_altura = sum(p['Altura'] for p in alunos_mais_13) / len(alunos_mais_13)
    print(f"{media_altura:.2f} metros")
    
    print("\nQuantidade de alunos com mais de 13 anos e altura abaixo da média:\n")
    contagem = sum(1 for p in alunos_mais_13 if p['Altura'] < media_altura)
    print(f"{contagem}")
    return media_altura, alunos_mais_13, contagem

         
# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    lista= entrada_usuario()
    exibir_resultados(lista)
    media, alunos_mais_13, contagem=analise_de_dados(lista)