import math

#Função calculaRaioDiametro recebe como parâmetro o diâmetro de um círculo, e obtém o raio a partir do diâmetro
def calculaRaioDiametro(diametro):
    #Retorna o valor do raio que é diametro / 2
    return diametro / 2

#Função calculaRaioArea recebe como parâmetro a área de um círculo, e obtém o raio a partir da área
def calculaRaioArea(area):
    #Fórmula da área do círulo é A = pi * raio²
    #Invertemos a fórmula para descobrir o valor do raio ao quadrado
    raioQuadrado = area / math.pi
    #Retornamos a raiz quadrada do raio ao quadrado para obter o valor do raio
    return math.sqrt(raioQuadrado)

#Função que calcula a área de um círculo dado o valor do raio do círculo
#Essa função foi criada só para conferir se o valor obtido pela função calculaRaioArea está correta
def calculaArea(raio):
    #Retorno do cálculo da fórmula da área do círculo (A = pi * raio²)
    return math.pi * math.pow(raio, 2)

#Variável área calcula a área de um círculo a partir de um raio 10
area = calculaArea(10)
#Variável raio calcula o raio de um círculo a partir da área. Essa variável deve ficar com o mesmo valor que foi passado como parâmetro na função calculaArea, no caso deste exemplo, o valor deve ser 10
raio = calculaRaioArea(area)

#Imprime resultados
print(area)
print(raio)