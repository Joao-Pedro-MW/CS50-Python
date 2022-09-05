def main():
    fracao = get_fracao("Qual a fração de combustível? ")
    if type(fracao) == str:
        return print(fracao)
    else:
        fracao = round(fracao)
        return print(f"{fracao}%")
def checa_valor(valor):
    fracao = fracao_para_lista(valor)
    if fracao == 100 or fracao == 99:
        fracao = "F"
    elif fracao == 0 or fracao == 1:
        fracao = "E"
    return fracao
def fracao_para_lista(valor):
    if "/" in valor:
        while True:
            try:
                fracao = valor.split("/")
                fracao = [int(x) for x in fracao]
                if fracao[0] > fracao[1]:
                    return main()
                while True:
                    try:
                        #calculamos a porcentagem do valor de combustível
                        fract = (fracao[0] / fracao[1]) * 100
                        return fract
                    except ZeroDivisionError:
                        pass
            except (ValueError,ZeroDivisionError):
                main()
    else:
        return main()
def get_fracao(prompt):
    while True:
        try:
            return checa_valor(str(input(prompt)))
        except ValueError:
            pass
main()
