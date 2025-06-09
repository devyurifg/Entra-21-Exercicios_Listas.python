'''Solicita o nome e as quatro notas de cada aluno, calcula a média e armazena as informações em uma lista.'''

# FUNÇÕES

def verificar_alunos():
    lista=[]
    for aluno in range (1,2):
        while True:
            entrada_aluno=input(f"Digite o nome do {aluno} aluno: ").strip()
            if entrada_aluno.replace(" ", "").isalpha():
                break
            else:
                print("Nome inválido! Digite um nome sem números ou símbolos.")
                
        notas=[]     
        for nota in range(1,5):
                while True:
                    entrada_nota=input(f"Digite a {nota}° de {entrada_aluno}: ")
                    try:
                        usuario_nota=float(entrada_nota)
                        if 0 <= usuario_nota <= 10:
                            notas.append(usuario_nota)
                            break
                        else:
                            print("Nota inválida!")
                    except ValueError:
                        print("Entrada inválida! Digite um número válido.")
                        
        media = sum(notas) / 4    
        lista.append({"Aluno": entrada_aluno, "Notas": notas, "Média": media})
        
    return lista
          
          
def exibir_resultados(lista):
    print()
    print(" Resultados dos alunos ".center(60, '-'))
    for i, aluno in enumerate(lista):
        nome = aluno["Aluno"]
        notas = ', '.join(f"{nota:.1f}" for nota in aluno["Notas"])
        media = aluno["Média"]
        print(f"{i+1} - {nome}: Notas = [{notas}] | Média = {media:.2f}")  
              
    print()
    
    print(" Alunos aprovados com média maior que 7 ".center(60, '-'))
    contador = 0
    for k, aluno in enumerate(lista):
        if aluno ["Média"] >=7:
            contador += 1
            print(f"{contador} - {aluno['Aluno']} com média {aluno['Média']:.2f}")
            
    if contador == 0:
        print("Nenhum aluno foi aprovado com média maior ou igual a 7.")
        
        
        

# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    lista= verificar_alunos()
    exibir_resultados(lista)