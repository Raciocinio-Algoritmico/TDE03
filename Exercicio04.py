#Função contaDigitos recebe como parâmetro um número qualquer
def contaDigitos(numero):
    #stringNumero armazena o numero recebido como parâmetro no formato string
    #fazemos isso pois não é possível utilizar o len() em tipos numéricos
    stringNumero = str(numero)
    #retornamos o tamanho do numero convertido em string
    return len(stringNumero)

#Variável quantidadeDigitos armazena o valor de retorno da função contaDigitos, que nesse caso será 5, pois o número passado como parâmetro é 12345 
quantidadeDigitos = contaDigitos(12345)
#Imprime o valor
print(quantidadeDigitos)