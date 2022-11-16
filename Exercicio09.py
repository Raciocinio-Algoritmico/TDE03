#Função calculaGorjeta recebe como parâmetro um valor qualquer referente ao total de uma conta de restaurante
def calculaGorjeta(valorConta):
    #Retorna 10% (0.1) do valor recebido como parâmetro
    return valorConta * 0.1

#Variáveis gorjeta1 e gorjeta2 armazenam o valor de retorno da função calculaGorjeta, que será 10.0 para gorjeta1, e 5.35 para gorjeta2
gorjeta1 = calculaGorjeta(100.0)
gorjeta2 = calculaGorjeta(53.50)

#Imprime os valores
print(gorjeta1)
#Esse segundo print diferentão é para limitar a quantidade de digitos depois do ponto no número float para 2. Se não ficaria aqueles números com vários digitos depois do ponto.
print('{:.2f}'.format(gorjeta2))
