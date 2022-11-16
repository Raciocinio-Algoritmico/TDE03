#Função criaListaVazua recebe como parâmetro o tamanho da lista
def criaListaVazia(tamanho):
    #Criando uma lista vazia (sem nada mesmo, nem zeros)
    lista = []
    #Para cada índice da lista até o tamanho (0 à 9)
    for i in range(tamanho):
        #Inserimos o valor 0 utilizando o append, que coloca o valor no final da lista
        lista.append(0)
    #Retorno da lista no tamanho solicitado por parâmetro preenchida com zeros
    return lista

#Função criaListaVazia1 recebe como parâmetro o tamanho da lista
#Uma forma alternativa mais simples de fazer a mesma coisa que a função criaListaVazia, sugerida pelo Eduardo Moura
def criaListaVazia1(tamanho):
    #Criamos uma lista preenchida com zeros pela multiplicação do valor 0 * tamanho informado por parâmetro
    lista = [0] * tamanho
    #Retorno da lista no tamanho solicitado por parâmetro preenchida com zeros
    return lista

#lista1 utiliza a primeira função criaListaVazia para armazenar uma lista de tamanho 10, que foi informada por parâmetro
lista1 = criaListaVazia(10)
#lista1 utiliza a segunda função criaListaVazia1 para armazenar uma lista de tamanho 10, que foi informada por parâmetro
lista2 = criaListaVazia1(10)

#Imprime as duas listas
print(lista1)
print(lista2)