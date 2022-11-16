#Função contaLetra recebe como parâmetro a palavra que será utilizada e a letra que deverá ser contada nesta palavra
def contaLetra(palavra, letra):
    #Variavel quantidadeLetra armazena a quantidade de vezes que uma letra aparece em uma palavra
    quantidadeLetra = palavra.count(letra)
    #Retorna a quantidade
    return quantidadeLetra

#Variáveis quantidade A, B e C, armazenam a quantidade de vezes que a letra a, b e c aparecem na string 'aaabbc'. Este valor é obtido a partir do retorno da função contaLetra
#quantidadeA será 3
#quantidadeB será 2
#quantidadeC será 1
quantidadeA = contaLetra('aaabbc', 'a')
quantidadeB = contaLetra('aaabbc', 'b')
quantidadeC = contaLetra('aaabbc', 'c')

#Imprime os valores
print(quantidadeA)
print(quantidadeB)
print(quantidadeC)