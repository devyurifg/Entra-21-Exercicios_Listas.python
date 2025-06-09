'''
O programa faz cinco perguntas relacionadas a um possível envolvimento em um crime, 
aceitando respostas "sim" ou "não". Após coletar as respostas, ele exibe todas as respostas registradas, 
conta quantas respostas positivas ("sim") foram dadas e classifica o usuário em uma das categorias:

- "Inocente" para 0 ou 1 resposta positiva.
- "Suspeita" para 2 respostas positivas.
- "Cúmplice" para 3 ou 4 respostas positivas.
- "Assassino" para 5 respostas positivas.
'''

#FUNÇÕES
def verificar_respostas():
    lista=[]
    for c in range(1):
        while True:
            telefonou_vitima=str(input("Telefonou para a a vítima? (sim/não): ")).strip().lower()
            if telefonou_vitima in ["sim", "não", "nao"]:
                lista.append({"Telefonou para vitima": telefonou_vitima})
                break
            else:
                print("Entrada inválida! Responda apenas com 'sim' ou 'não'.")
        
        while True:        
            local_crime=str(input("Esteve no local do crime? (sim/não): ")).strip().lower()
            if local_crime in ["sim", "não", "nao"]:
                lista.append({"Esteve no local do crime": local_crime})
                break
            else:
                print("Entrada inválida! Responda apenas com 'sim' ou 'não'.")
        
        while True:        
            mora_perto_vitima=str(input("Mora perto da vítima? (sim/não): ")).strip().lower()
            if mora_perto_vitima in ["sim", "não", "nao"]:
                lista.append({"Mora perto da vítima": mora_perto_vitima})
                break
            else:
                print("Entrada inválida! Responda apenas com 'sim' ou 'não'.")
         
        while True:        
            divida_vitima=str(input("Devia para a vítima? (sim/não): ")).strip().lower()
            if divida_vitima in ["sim", "não", "nao"]:
                lista.append({"Devia para a vítima": divida_vitima})
                break
            else:
                print("Entrada inválida! Responda apenas com 'sim' ou 'não'.")
           
        while True:        
            trabalho_vitima=str(input("Já trabalhou com a vítima? (sim/não): ")).strip().lower()
            if trabalho_vitima in ["sim", "não", "nao"]:
                lista.append({"Já trabalhou com a vítima": trabalho_vitima})
                break
            else:
                print("Entrada inválida! Responda apenas com 'sim' ou 'não'.")
        return lista


def exibir_resultados(lista):
    print("\nRespostas registradas:\n")
    contador_sim = 0
    for item in lista:
        for pergunta, resposta in item.items():
            print(f"{pergunta}: {resposta}")
            if resposta == "sim":
                contador_sim += 1

    print(f"\nTotal de respostas 'sim': {contador_sim}\n")

    if contador_sim == 5:
        classificacao = "Assassino"
    elif 3 <= contador_sim <= 4:
        classificacao = "Cúmplice"
    elif contador_sim == 2:
        classificacao = "Suspeito"
    else:
        classificacao = "Inocente"

    print(f"Classificação: {classificacao}")  
            
        
#PROGRAMA PRINCIPAL
if __name__ == "__main__":
    lista=verificar_respostas()
    exibir_resultados(lista) 
    