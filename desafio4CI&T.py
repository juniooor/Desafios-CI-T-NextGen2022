'''
Dada um texto qualquer e um lista de termos de pesquisa (sequencia de caracteres), retorne os
primeiros K termos mais recorrentes na string, onde K é um parâmetro configurável.
Exemplo:
String: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua"
Lista de termos: ["a", "em", "i", "el"]
K: 2
Resultado: ["i", "a"]
Explicação:
Ocorrências de cada termo,"i": 11, "a": 7, "em": 2, "el": 1, com K = 2, retornamos "i" e "a" ordenados conforme 
a quantidade de ocorrências de cada termo.
Obs: Quando houver termos com quantidades iguais, priorizar o retorno de acordo com a ordem de ocorrência do termo 
na string.
'''
from collections import Counter
def calcula_top_ocorrencias_de_queries(texto,queries,k):
    resultado=[]
    # print(Counter({o:texto.count(o) for o in queries}))
    c = Counter({o:texto.count(o) for o in queries}).most_common(k)
    for i in c:
        resultado.append(i[0])
    return resultado
        

    
    




if __name__ == '__main__':
    a = calcula_top_ocorrencias_de_queries("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",["a","em","i","el"],2)
    print(a)