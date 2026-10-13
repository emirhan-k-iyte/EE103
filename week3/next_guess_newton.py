x = float(input("What x to find the cube root of? "))
g = float(input("What guess to start with? "))

print(f"Current estimate cube: {g ** 3}")

next_guess = g - (g ** 3 - x) / (3 * g ** 2)

print(f"Next guess: {next_guess}")