from secret_number import secretNum

while True:
    guess = int(input("Guess the secret number: "))

    if guess < secretNum:
        print("Too low")
    elif guess > secretNum:
        print("Too high")
    else:
        print("Correct!")
        break