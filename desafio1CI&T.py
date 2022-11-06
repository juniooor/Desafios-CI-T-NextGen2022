'''Você e seu time estão desenvolvendo um sistema de indicações de postos de gasolina que ficam próximos da localização atual do veículo. No modo de direção “viagem”, a funcionalidade a ser desenvolvida é de indicar ao condutor o posto mais distante possível dentro do limite atual de combustível. E caso não exista posto de gasolina, retornar -1

A pessoa responsável por fazer a especificação do sistema informou que você terá as seguintes informações: consumo médio de combustível, quantidade de combustível restante no veículo e um array contendo distâncias dos postos de gasolinas.

Exemplo:
Combustivel (em litros): 2
Consumo médio (km/l): 8
Postos de Gasolina (km): [2, 15, 22, 10.2]'''



def ultima_parada(combustivel,consumo,postos_de_gasolina):
    distancia = combustivel * consumo
    prox = postos_de_gasolina[min(range(len(postos_de_gasolina)), key = lambda i: abs(postos_de_gasolina[i]-distancia))]
    if distancia < prox:
        return -1
    else:
        return prox


if __name__ == '__main__':
    posto = ultima_parada(3,2,[19,15,22,11])

    print(posto)

# combustivel =  2
# consumo = 8
# postos_de_gasolina= [2, 15, 22, 10.2]