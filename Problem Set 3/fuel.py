def main():
    fracao = gauge(convert(input("Qual a fração de combustível? ")))
    print(fracao)
def convert(fraction):
        if "/" in fraction:
            try:
                fraction = fraction.split("/")
                dividendo, divisor = 0,0
                dividendo = fraction[0]
                divisor = fraction[1]
                if divisor.isnumeric() and dividendo.isnumeric():
                    divisor = int(divisor)
                    dividendo = int(dividendo)
                    if divisor == 0:
                        raise ZeroDivisionError
                    if dividendo > divisor:
                        raise ValueError
                    else:
                        #calculamos a porcentagem do valor de combustível
                        fraction = (dividendo / divisor) * 100
                        return int(fraction)
                else:
                    raise ValueError
            finally:
                pass
        else: return int(fraction)
def gauge(percentage):
    if percentage >= 99:
        percentage = "F"
        return percentage
    elif percentage <= 1:
        percentage = "E"
        return percentage
    return f"{percentage}%"
if __name__ == "__main__":
    main()
