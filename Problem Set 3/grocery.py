grocery = dict()
def groceries():
    while True:
        try:
            item = input().upper()
            val = 0
            if item in grocery:
                #somamos 1 a cada input já existente
                val = grocery[item] + 1
                grocery.update({item:val})
            else:
                #se o input n existe, o criamos
                grocery.update({item:1})
        except EOFError:
            #convertemos em uma lista para ordenar os items em ordem alfabética
            items = list(grocery)
            items.sort()
            for i in items:
                print(grocery[i],i)
            break
groceries()