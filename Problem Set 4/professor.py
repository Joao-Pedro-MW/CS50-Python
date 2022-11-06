from random import randint
#from random import seed
def main():
    level = get_level()
    counter = 0
    correct_answers = 0
    while counter <= 9:
        #check the answer for 10 equations
        tries = 0
        equation = generate_integer(level)
        counter += 1
        while tries < 3:
            try:
            #verify the number os tries of answer
                user_input = int(input(f"{equation[0]} + {equation[1]} = "))
                if user_input == equation[2]:
                    #if correct
                    correct_answers += 1
                    break
                else:
                    #if wrong
                    tries += 1
                if tries == 3:
                    #if the number os tries is 3 the program return the correct answer
                    print("EEE")
                    print(f"{equation[0]} + {equation[1]} = {equation[2]}")
                    break
                else:
                    #if it's not the 3rd time ir just returns EEE
                    print("EEE")
            except ValueError:
                pass
    return print("Score: ",correct_answers)
def get_level():
    #verify a user input for level
    levels = [1,2,3]
    try:
        level = int(input("Level: "))
    except ValueError:
        get_level()
    if level not in levels:
        get_level()
    return level
def generate_integer(level):
    #generates a random equation that returns X, Y and the answer
    if level == 1:
        X = randint(0,9)
        Y = randint(0,9)
    elif level == 2:
        X = randint(10,99)
        Y = randint(10,99)
    elif level == 3:
        X = randint(100,999)
        Y = randint(100,999)
    answer = X + Y
    values = [X,Y,answer]
    return values
if __name__ == "__main__":
    main()