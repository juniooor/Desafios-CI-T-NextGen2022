'''Durante uma expedição tecnológica, sua equipe encontrou o que parece ser a senha que lhes dá acesso
a um grande tesouro digital. Por sorte, sua equipe é formada pelas pessoas mais feras em programação e 
vocês rapidamente descobriram como decifrá-la.Com a possibilidade de que vocês encontrem mais códigos contendo 
outras senhas, você foi designado à tarefa de desenvolver um algoritmo que decifra os códigos para não precisarem
fazer isso de forma manual.A senha é representada por um número binário de 10 dígitos formado pelo dígito predominante
de cada coluna. Caso a coluna tenha a mesma quantidade de dígitos 0 e 1, deve se considerar o número 1.Exemplo:
A primeira coluna da lista tem como dígito predominante o número 1, sendo assim, 
o primeiro dígito - dos 10 - da senha é 1.

0 1 1 0 1 0 0 0 0 0
1 0 0 1 0 1 1 1 1 1
1 1 1 0 0 0 1 0 1 0
0 1 1 1 0 1 0 1 0 1
0 0 1 1 1 0 0 1 1 0
1 0 1 0 0 1 1 0 0 1
1 1 0 1 1 0 0 1 0 0
1 0 1 1 0 1 0 1 0 0
1 0 0 1 1 0 0 1 1 1
1 0 0 0 0 1 1 0 0 0

1 0 1 1 0 1 0 1 0 0 

Desenvolva um algoritmo que receba um array de valores binários (como o exemplo acima) e retorne 
a representação decimal da senha.'''

def calcula_numero_da_senha(senha):
    valor_binario = []
    for t in zip(senha[0],senha[1],senha[2],senha[3],senha[4],senha[5],senha[6],senha[7],senha[8],senha[9]):
        a = t.count('1')
        b = t.count('0')
        if a >= b:
            valor_binario.append('1')
        elif a < b:
            valor_binario.append('0')
    valorBinario = ''.join(valor_binario)
    decimal = int(valorBinario, 2)
    return decimal
            
    






if __name__ == '__main__':

    a = calcula_numero_da_senha(["0110100000","1001011111","1110001010","0111010101","0011100110","1010011001","1101100100","1011010100","1001100111","1000011000"])
