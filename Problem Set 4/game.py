from random import randint
while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            pass
        else:
            number = randint(1,level)
            break
    except ValueError:
        pass
while True:
    try:
        guess = int(input("Guess: "))
        if guess == number:
            print("Just right!")
            break
        elif guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
    except ValueError:
        pass