'''Dizemos que um número natural X esconde o Y quando, ao apagar alguns algarismos de X, o número Y aparece. 
Por exemplo, o número 12345 esconde o número 235, uma vez que pode ser obtido ao apagar os números 1 e 4.
Por outro lado, ele não esconde o número 154.
A imagem demonstra números: 1,2,3,4,5 todos estão em azul, mas o número 1 e 4 estão com um risco vermelho.
Escreva um código que recebe dois números e que retorna um booleano dizendo se o primeiro esconde o segundo.'''

def checa_numero_escondido(numero,numero_oculto):
    numero = str(numero)
    numero_oculto = str(numero_oculto)
    for num in numero_oculto:
        if num not in numero:
            return False
    return True

        


if __name__ == '__main__':
    
    a = checa_numero_escondido(12345,235)