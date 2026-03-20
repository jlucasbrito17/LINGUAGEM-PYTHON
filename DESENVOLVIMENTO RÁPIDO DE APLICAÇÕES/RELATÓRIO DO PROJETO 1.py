# Python docs 
#   - online em https://python.org/doc ou https://docs.python.org/pt-br/3.10/#
#   - Download: https://docs.python.org/pt-br/3.10/download.html
#   - Especificamente sobre arquivos: https://docs.python.org/pt-br/3.10/tutorial/inputoutput.html#reading-and-writing-files

#==============================================
# Manipulacao de Arquivos em Python ===========
#==============================================

#-- 1 ---------------------------------------------------------------------------------------------------------
# Abrindo arquivo existente
#   A funcao open(path, mode) recebe dois parametros: path e mode. O primeiro se refere ao caminho de onde esta
# o arquivo a ser aberto. Ja o segundo, se refere ao modo de acesso. A seguir, alguns modos de acesso:
#   - r : read / leitura
#   - w : write / escrita -> sobrescreve ou cria um novo
#   - r+ : read and write / leitura + escrita
#   - w+ : write and read / escrita + leitura
#   - a : append / acrescenta no fim
#   - a+ : append / acrescento no inicio
#
#                     | r   r+   w   w+   a   a+
#   ------------------|--------------------------
#   read              | +   +        +        +
#   write             |     +    +   +    +   +
#   write after seek  |     +    +   +
#   create            |          +   +    +   +
#   truncate          |          +   +
#   position at start | +   +    +   +
#   position at end   |                   +   +  
#
#   'after seek': significa que vocc pode definir o byte onde vai comecar a operacao. Por exemplo: arquivo.write(2).
#   'truncate': significa que o arquivo vai ser sobrescrito.
#   
#   Como estou utilizando o VSCode, tenho como workspace a pasta VS_Workspace, o qual e tido como o inicio do caminho 
# (path). Portanto, basta escrever o caminho do arquivo dentro do workspace.
#
#   A funcao open() retorna o arquivo pedido, com o respectivo modo de acesso. Por isso e necessario uma variavel para 
# 'receber' esse arquivo. No nosso caso, o nome da variavel e 'arquivo', mas poderia ser qualquer outra palavra, desde 
# que nao seja alguma ja reservada (exemplo de palavra reservada: if). A partir de entao, e possivel manipular o arqui
# vo a partir da variavel.
#
#  E interessante sempre escrever logo o '.close()', para evitar problemas. Caso a execucao seja interrompida, ou fina
# lizada normalmente, sem que o arquivo seja fechado, voce tera problemas para acessa-lo, mesmo com outro programa, como 
# o bloco de notas.
#
##arquivo = open("RAD em Python/teste.txt", "r")
#
##print(arquivo.readable())  # imprimindo a verificacao se o arquivo pode ser lido
##print(arquivo.read())      # imprimindo o arquivo
#
#   readline() le uma linha e deixa o 'cursor' na linha seguinte. Portanto, uma sequencia de readline() vai retornar sem
# pre a linha seguinte. Com o print(), a leitura de cada linha e impressa. Como cada linha do arquivo que esta sendo lido 
# termina com '\n' (quebra de linha) o resultado de cada readline() vai ter a seguir uma linha em branco.
#
##print(arquivo.readline())
##print(arquivo.readline())
##print(arquivo.readline())
#
#   A funcao readlines() retorna uma lista, onde cada elemento da lista e o conteudo de uma linha. Essa lista esta sendo ar
# mazenada na variavel lista. A partir dai podemos manipular a lista. Perceba que manipulando a lista, mesmo que apagando ele
# mentos, nao vai afetar o arquivo.
#
##lista = arquivo.readlines()
##print(lista)
#
#   Outra maneira de imprimir uma lista e utilizando o comando for. Da maneira que foi escrita, este for funciona como o 'for 
# each' (para cada) de outras linguagens. Entao, o codigo esta dizendo mais ou menos assim: para cada elemento da lista, visto 
# como l : ...
#
#   Outra peculiaridade do Python e a sua necessidade de identacao. Isto porque, como voce ja deve ter notado, nao temos ponto 
# e virgula para definir o fim de uma linha, ou { e } para definir o escopo de um bloco. Portanto, todo bloco em Python inicia 
# com a 'chamada' do bloco seguido de dois pontos. No nosso caso, a 'chamada' e o for, ou seja, a chamada de um bloco de 
# repeticao. Seguido do for temos o :. Apos os dois pontos, para que o interpretador do Python saibda que uma linha faz parte do bloco,
# e necessario que aquela linha comece 'tabulada', ou seja, deslocada para o lado. Por isso, o print(l) e visto como uma linha 
# dentro do for. A primeira apos o bloco cujo codigo nao esteja deslocado, o interpretador ja vai entender como um comando que não
# pertence ao for.
#
##for l in lista: 
##    print(l)
#
##arquivo.close()
#--------------------------------------------------------------------------------------------------------------

#-- 2 ---------------------------------------------------------------------------------------------------------
#   Abrinda um arquivo existente com o modo de acesso 'append'. A partir disso e possivel acrescentar conteudo ao arquivo. No 
# nosso caso, criamos um comando para que fosse escrito "\nSQL". Quando o arquivo e aberto em modo 'a' a nova escrita vai ini
# ciar no espaco seguinte ao ultimo ja existente. No nosso exemplo, em teste.txt, tinhamos como ultimo elemento a palavra Matlab.
# Com o append, a nova escrita comecaria colado ao Matlab. Porem, como escrevemos o \n, vai haver primeiro uma quebra de linha. 
# O SQL e escrito logo apos a quebra de linha.
#
##arquivo = open("RAD em Python/teste.txt", "a")
##arquivo.write("\nSQL")
##arquivo.write("\nR\n")
##arquivo.close()
#--------------------------------------------------------------------------------------------------------------

#-- 3 ---------------------------------------------------------------------------------------------------------
#  Caso o modo de escrita seja 'selecionado', e o arquivo pedido nao exista, entao ele sera criado. E importante lembrar tambem
# que, caso o arquivo ja exista, com este modo de acesso, o coonteudo dele sera sobrescrito.
#
##arquivo = open("RAD em Python/teste2.txt", "w")
##arquivo.write("Portugol\n")
##arquivo.write("ADA\n")
##arquivo.write("C#")
##arquivo.close()
#--------------------------------------------------------------------------------------------------------------

#-- 4 ---------------------------------------------------------------------------------------------------------
#   A remocao de arquivos pode ser feita com a importacao do modulo 'os' (de operating system, ou sistema operacional).
# Esse modulo prove uma interface para funcionalidades dependentes do sistema operacional.
#
##import os # Apesar de ser nativo do Python, precisa ser explicitamente importado
#
#   Verificando se um arquivo existe. Caso positivo, o arquivo e removido. Senao, e impressa a mensagem.
##if os.path.exists("RAD em Python/teste3.txt"):
##    os.remove("RAD em Python/teste3.txt")
##else:
##    print("ESTO NON ECZISTE")
#--------------------------------------------------------------------------------------------------------------

#-- 5 ---------------------------------------------------------------------------------------------------------
# Da mesma forma, ou seja, com o uso do modulo 'os', e possivel criar e remover pastas. Entretanto, a remocao so e
# possivel se a pasta estiver vazia.
#
##os.mkdir("RAD em Python/TESTE")
##os.rmdir("RAD em Python") # So remove se estiver vazia