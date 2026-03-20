# Python docs: online em https://python.org/doc ou https://docs.python.org/pt-br/3.10/#
#       - Download: https://docs.python.org/pt-br/3.10/download.html
#       - Especificamente sobre arquivos: https://docs.python.org/pt-br/3.10/tutorial/inputoutput.html#reading-and-writing-files

r - read / leitura
a - append / acrescenta
w - write / escrita -> sobrescreve ou cria um novo
x - create / criar arquivo
r+ - read and write / leitura + escrita

#-- 1 --------------------
arquivo = open("RAD em Python/teste.txt", "r")

#-- 2 --------------------

arquivo = open("RAD em Python/teste.txt", "a")

#-- 3 --------------------

arquivo = open("RAD em Python/teste2.txt", "w")

#-- 4 --------------------

arquivo = open("RAD em Python/teste2.txt", "r")

#-- 5 --------------------

arquivo = open("RAD em Python/teste3.txt", "x")

#== 1 ====================

print(arquivo.readable())
print(arquivo.read())

#== 2 ====================

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

#== 3 ====================

lista = arquivo.readlines()
print(lista)

for l in lista: 
    print(l)

#== 4 ====================

arquivo.write("\nSQL")
arquivo.write("\nR")

#== 5 ====================

arquivo.write("Portugol\n")
arquivo.write("ADA\n")
arquivo.write("C#")

arquivo.write("Mermao!\n")

#-- 1 ao 5 ----------------

arquivo.close()

#== 6 ====================

import os

# Remover arquivo

if os.path.exists("RAD em Python/teste3.txt"):
    os.remove("RAD em Python/teste3.txt")
else:
    print("ESTO NON ECZISTE")

# Remover pasta

os.rmdir("RAD em Python") # Só remove se estiver vazia

# Criar pasta

os.mkdir(PATH)