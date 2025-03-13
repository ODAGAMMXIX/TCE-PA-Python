def f(arg1, arg2, arg3):                                 # arg1: string / arg2: inteiro / arg3: inteiro.
    aux = []                                             #Inicializa uma lista vazia aux que armazenará as letras convertidas.
    for i in arg1.upper():                               #Converte arg1 para maiúsculas e itera sobre cada letra.
        if ord(i) + arg3 > ord('Z'):                     #Verifica se a soma do valor ASCII da letra i com arg3 excede o valor ASCII de 'Z'.
            r = ord(i) + arg3 - (ord('Z') - ord('A')) - 1 #Se exceder, ajusta o valor para permanecer dentro do intervalo de letras maiúsculas.
        else:
            r = ord(i) + arg3                            #Caso contrário, apenas soma arg3 ao valor ASCII da letra i.
        aux += [chr(r)]                                  #Converte o valor ASCII r de volta para a letra correspondente e adiciona à lista aux
        arg3 += 1                                        #Incrementa arg3.
        if arg3 == arg2 + 1:                             #Se arg3 atingir o valor arg2 + 1, reseta arg3 para 1.
            arg3 = 1                                  #Concatena a lista aux em uma string e retorna.
    return "".join(aux)                                  #

if __name__ == '__main__':                                  #
    s = input()                                  #
    n = int(input())                                  #
    c = int(input())                                  #
    print(f(s, n, c))                                  #
