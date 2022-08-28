camelCase = input("Informe a variável: ")
i,words = 0,list()
txt = ""
for _ in camelCase:
    if _.isupper():
        #separamos a nossa palavra
        word = camelCase[i:camelCase.index(_)]
        #formatamos a palavra com texto minusculo e um _ no final
        word = word.lower() + "_"
        #adicionamos nossa palavra a lista principal
        words.append(word)
        #colocamos i para iniciar no final da palavra anterior
        i = camelCase.index(_)
#adicionamos a última palavra da variável já formatada com texto minusculo
words.append((camelCase[i::]).lower())
#adicionamos todas as palavras a uma só usando nosso txt
print(txt.join(words))
