'''
- Solicita ao usuário que insira a temperatura média de cada mês do ano de 2025.
- Armazena em uma lista com 12 valores do tipo float, representando as temperaturas médias de cada mês.
- Retorna a lista com as temperaturas dos meses, média anual das temperaturas e indica os meses com temperaturas acima da média.
'''

# FUNÇÕES

def verificar_temperatura():
    lista=[]
    for mes in range(1,13):
        while True:
            entrada=input(f"Digite a temperatura média do {mes}° mês de 2025: ")
            try:
                entrada_usuario=float(entrada.replace(",", "."))
                lista.append(entrada_usuario)
                break
            except ValueError:
                print("Entrada inválida! digite apenas um número inteiro")
    return lista   


def exibir_resultados(lista):
    meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    print("\nTemperaturas médias de 2025:")
    for i, temp in enumerate(lista):
        print(f"{meses[i]}: {temp:.1f}°C")        


def analise_de_dados(lista):
    meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    media= sum(lista) / len(lista)
    print(f"\nMédia anual das temperaturas: {media:.1f}°C\n")
    
    print("Meses com temperatura acima da média:")
    for i, temp in enumerate(lista):
        if temp > media:
            print(f"{i+1} – {meses[i]}: {temp:.1f}°C")
    return media        
    
    
# PROGRAMA PRINCIPAL

if __name__ == "__main__":    
    lista=verificar_temperatura()
    exibir_resultados(lista)
    media=analise_de_dados(lista)