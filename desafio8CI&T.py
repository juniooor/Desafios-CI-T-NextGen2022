'''Um grande amigo seu mora numa cidade pequena, onde existem apenas duas empresas de táxi - a Empresa 1 e a Empresa 2.
Ambas mudam suas taxas a cada dia e calculam o valor de suas corridas da seguinte forma: uma taxa fixa mais um valor por
quilômetro rodado.Seu amigo é fisioterapeuta e pega táxis diariamente para visitar seus clientes ao redor da cidade.
Você decidiu escrever um código para ajudá-lo a decidir qual empresa escolher para cada uma das corridas, baseado no 
preço.Sua função receberá 4 valores: TF1 (a taxa fixa da empresa 1), VQR1 (o valor por quilômetro rodado da empresa 1),
TF2 (a taxa fixa da empresa 2), VQR2 (o valor por quilômetro rodado da empresa 2), todos em formato string. 
Seu retorno deve ser uma string em uma das seguintes formas:
“Tanto faz” - para o caso de o valor das duas empresas para qualquer corrida ser igual
“Empresa 1” - se o valor da Empresa 1 for sempre menor que o da Empresa 2
“Empresa 2” - para o caso contrário do citado acima
“Empresa Xpto quando a distância < N, Tanto faz quando a distância = N, Empresa Ypto quando a distância > N” para o caso de a escolha depender da distância a ser percorrida (onde Xpto e Ypto representa 1 ou 2 e N representa a distância).
Exemplo:
TF1 = 2,50
VQR1 = 1,00
TF2 = 5,00
VQR2 = 0,75
Output:
“Empresa 1 quando a distância < 10.0, Tanto faz quando a distância = 10.0, Empresa 2 quando a distância > 10.0”'''

def escolhe_taxi(tf1,vqr1,tf2,vqr2):
    tf1 = float(tf1)
    vqr1 = float(vqr1)
    tf2 = float(tf2)
    vqr2 = float(vqr2)
    if tf1 == tf2 and vqr1 == vqr2:
        return  'Tanto faz'    
    
    elif tf1 <= tf2 and vqr1 <= vqr2:
        return  'Empresa 1'
    
    elif tf1 >= tf2 and vqr1 >= vqr2:
        return  'Empresa 2'
    
    else:
        N = ((tf1 - tf2) / (vqr2 - vqr1))
        valor1 = tf1 + vqr1 * (N-1)
        valor2 = tf2 + vqr2 * (N-1)
        if valor1 < valor2:
            xpto = 1
        else:
            xpto = 2
        if xpto == 1:
            ypto = 2
        else:
            ypto = 1
    
    return f' Empresa {xpto} quando a distância < {str(N)}, Tanto faz quando a distância = {str(N)}, Empresa {ypto} quando a distância > {str(N)}'

if __name__ == '__main__':
    a = escolhe_taxi("2.5","1.0","5.0","0.75")
    print(a)