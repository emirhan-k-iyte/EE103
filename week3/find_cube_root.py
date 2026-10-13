given_number = int(input("Enter an integer: "))

target = abs(given_number)
guess_number = 0

while guess_number ** 3 < target:
    guess_number += 1

if guess_number ** 3 == target:
    if given_number < 0:
        guess_number = -guess_number

    print(f"Cube root: {guess_number}")
else:
    print(f"{given_number} is not a perfect cube.")