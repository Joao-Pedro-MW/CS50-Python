from PIL import Image
import PIL
from sys import argv as cli_args
from sys import exit as finalizar

img_extensions = ["jpg", "png", "jpeg"]
if len(cli_args) <= 1:
    finalizar("Too few command-line arguments")
elif len(cli_args) != 3:
    finalizar("Too many command-line arguments")

input_image = cli_args[1].strip().lower()
output_image_name = cli_args[2].strip().lower()

if output_image_name.split(".")[1] not in img_extensions:
    finalizar("Invalid output")
if output_image_name.split(".")[1] != input_image.split(".")[1]:
    finalizar("Input and output have different extensions")

#abrimos o arquivo q contem a imagem da camisa CS50
cs50_shirt = Image.open("shirt.png")
#tratamos a nossa imagem como um arquivo PNG pois assim removemos o fundo dela
cs50_shirt = cs50_shirt.convert("RGBA")

try:
    # abrimos nossa imagem
    with Image.open(input_image) as user_image:
        output_image = user_image.copy()
        # Modelamos a nossa imagem e alteramos suas dimensões
        output_image = PIL.ImageOps.fit(output_image, size=(600, 600))
        # vamos unir a foto com a camisa
        # Passamos a mesma imagem 2x pois o primeiro é a imagem que desejamos sobrepor
        # O segundo argumento é a mascara que usamos na imagem
        output_image.paste(cs50_shirt,cs50_shirt)
        # salvamos a imagem
        output_image.save(output_image_name)
except FileNotFoundError:
    finalizar("Input does not exist")
