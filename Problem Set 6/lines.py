#um programa que pega um input de nome do arquivo da linha de comando
#depois abre o arquivo e conta o número de linhas
# se começa com # ou " " deve ser ignorado, por ser comentário ou linha vazia
from sys import argv as arquivo
from sys import exit as finalizar
if len(arquivo) <= 1:
    finalizar("Too few command-line arguments")
elif len(arquivo) != 2:
    finalizar("Too many command-line arguments")
arquivo = arquivo[1]
if ".py" not in arquivo:
    finalizar("Not a Python file")
try:
    with open(arquivo,"r") as arquivo_python:
        counter = 0
        #checamos cada linha do arquivo
        for linha in arquivo_python:
            #vemos se uma linha tem apenas espaços em branco
            if not linha.isspace():
                 #vamos se não existem # no inicio da linha
                if not linha.strip().startswith("#"):
                    counter += 1
except FileNotFoundError:
    finalizar("File does not exist")
print(counter)
