from sys import argv as arquivo
from sys import exit as finalizar
from tabulate import tabulate
import csv
if len(arquivo) <= 1:
    finalizar("Too few command-line arguments")
elif len(arquivo) != 2:
    finalizar("Too many command-line arguments")
arquivo = arquivo[1]
if ".csv" not in arquivo:
    finalizar("Not a CSV file")

pizzas = []
try:
    with open(arquivo,"r") as arquivo_python:
        arquivo_python = csv.reader(arquivo_python)
        for linha in arquivo_python:
            pizzas.append(linha)
except FileNotFoundError:
    finalizar("File does not exist")
titulo = pizzas[0]
del pizzas[0]
print(tabulate(pizzas, headers=titulo, tablefmt="grid"))