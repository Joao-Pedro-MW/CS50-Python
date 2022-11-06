import inflect
inflect = inflect.engine()
names = list()
try:
    while True:
        name = str(input("Name: "))
        names.append(name)
except EOFError:
    names = inflect.join(names)
    print("Adieu, adieu, to",names)
