#Função concatenaPalavras recebe como parâmetro duas palavras quaisquer
def concatenaPalavras(palavra1, palavra2):
    #Variável stringConcatenada armazena a junção das duas palavras recebidas como parâmetro
    stringConcatenada = palavra1 + palavra2
    #Retornamos o resultado da concatenação (junção) das strings
    return stringConcatenada

#Variável palavra armazena o valor retornado da função concatenaPalavras, que nesse caso será 'Boa prova!', pois o retorno da função concatenaPalavras será a concatenação (junção) das duas palavras passadas como parâmetro
palavra = concatenaPalavras('Boa ', 'prova!')

#Imprime resultado
print(palavra)
