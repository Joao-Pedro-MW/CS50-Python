from sys import argv as arquivo
from sys import exit as finalizar
import csv

if len(arquivo) <= 1:
    finalizar("Too few command-line arguments")
elif len(arquivo) != 3:
    finalizar("Too many command-line arguments")
output = arquivo[2]
arquivo = arquivo[1]

try:
    # abrimos o csv dos dados
    with open(arquivo, "r", newline="") as arquivo_csv:
        reader = csv.DictReader(arquivo_csv)
        # abrimos/criamos nosso csv contendo os novos dados
        with open(output, "w+", newline="") as arquivo_saida:
            # instanciamos o método de escrever linhas no novo arquivo
            writer = csv.writer(arquivo_saida)
            # escrevemos os títulos das colunas
            writer.writerow(["first", "last", "house"])
            for row in reader:
                # pegamos os nomes completos e separamos em primeiro e segundo nome
                complete_name = row["name"].split(",")
                # removemos os espaços
                last, name = complete_name[0].strip(), complete_name[1].strip()
                # escrevemos a linha no formato nome, sobrenome, casa
                writer.writerow([name, last, row["house"]])
except FileNotFoundError:
    finalizar("Could not read invalid_file.csv")
