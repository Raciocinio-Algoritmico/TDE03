#Função verificaNumeroPar recebe como parâmetro um número qualquer
def verificaNumeroPar(numero):
    #Se o numero recebido for par
    if numero % 2 == 0:
        #Então o retorno é True (verdadeiro)
        return True
    #Caso o numero recebido não for par
    else:
        #Então o retorno é False (falso)
        return False

#numero1 irá armazenar o valor booleano True do retorno da função, pois o número passado como parâmetro para a função verificaNumeroPar é 6, que é par
numero1 = verificaNumeroPar(6)
#numero2 irá armazenar o valor booleano False do retorno da função, pois o número passado como parâmetro para a função verificaNumeroPar é 5, que é ímpar
numero2 = verificaNumeroPar(5)

#Imprimimos o resultado
print(numero1)
print(numero2)