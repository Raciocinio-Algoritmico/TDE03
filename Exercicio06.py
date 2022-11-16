#Função imprimeNomes recebe como parâmetro uma lista de nomes
def imprimeNomes(nomes):
    #Para cada nome na lista nomes
    for nome in nomes:
        #Imprime o nome
        print(nome)

#Lista meninas contém o nome de todas as meninas da disciplina de Raciocínio Algorítmico
meninas = ['Marina', 'Mariana', 'Caroline', 'Mel', 'Julia', 'Victoria']

#Chama a função que executa o print dos nomes da lista
#Funções como a função imprimeNome, que não possuem retorno, não devem ser armazenadas em variáveis, pois não terá nenhum valor para ser armazenado. Esse tipo de função apenas executa um trecho de código que foi definido dentro do escopo da função
imprimeNomes(meninas)