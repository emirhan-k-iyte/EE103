from secret_number import secretNum

attempts = 0
found = False

while True:
    guess = int(input(f"Guess the secret number ({attempts + 1}/5): "))
    attempts += 1

    if guess < secretNum:
        print("Too low")
    elif guess > secretNum:
        print("Too high")
    else:
        print("Correct!")
        found = True
        break

    if attempts == 5:
        break

if not found:
    while True:
        print("Oh! Noooooo...")