from pyfiglet import Figlet
import sys
from random import choice
figlet = Figlet()
#creates a list for the available fonts
font_list = figlet.getFonts()
font_commands = ["-f","--fonts"]
font_style = choice(font_list)
figlet.setFont(font=font_style)
def ascii():
    try:
        #check if the command line for arguments is valid
        if sys.argv[-1] not in font_list:
            sys.exit("Invalid usage")
        else:
            font_style = sys.argv[-1]
        #check if the font is valid for the system
        if str(sys.argv[1]) not in font_commands:
            sys.exit("Invalid usage")
    except IndexError:
            sys.exit("Invalid usage")
    text = str(input("Text: "))
    figlet.setFont(font=font_style)
    return print(figlet.renderText(text))
def validate_command(command_line_arguments):
    if len(sys.argv) == 1:
        text = str(input("Text: "))
        return print(figlet.renderText(text))
    elif len(sys.argv) != 3:
        sys.exit("Invalid usage")
    else:
        ascii()
def main():
    validate_command(sys.argv)
main()