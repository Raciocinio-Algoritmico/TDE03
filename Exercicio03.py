#Função verificaNumeroPositivo recebe como parâmetro um número qualquer
def verificaNumeroPositivo(numero):
    #Se o número for maior ou igual a zero
    if numero >= 0:
        #Então o retorno da função é 'P' pois o número é positivo
        return 'P'
    #Se o número for menor do que zero
    else:
        #Então o retorno da função é 'N' pois o número é negativo
        return 'N'

#Variável numero1 armazena o valor de retorno da função verificaNumeroPositivo, que sera 'P' pois o número passado como parâmetro é 1, que é positivo
numero1 = verificaNumeroPositivo(1)
#Variável numero2 armazena o valor de retorno da função verificaNumeroPositivo, que sera 'N' pois o número passado como parâmetro é -1, que é negativo
numero2 = verificaNumeroPositivo(-1)

#Imprime os valores
print(numero1)
print(numero2)