#Função contarCaracteres que recebe como parâmetro uma palavra qualquer
def contarCaracteres(palavra):
    #Salva o tamanho da palavra em uma variável utilizando len (que vem do length em inglês, que significa tamanho em português)
    tamanho = len(palavra)
    #retorna o tamanho (agora podemos fazer contas com esse valor ou armazená-lo em variáveis)
    return tamanho


#Salva o tamanho que foi retornado da função na variável quantidadeCaracteres
#O tamanho deve ser 6, pois a palavra (string) que foi passada como parâmetro é 'Marina'
quantidadeCaracteres = contarCaracteres('Marina')
#Imprime o valor
print(quantidadeCaracteres)