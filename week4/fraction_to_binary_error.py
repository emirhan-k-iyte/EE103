target = float(input("Enter a fraction (0 <= F < 1): "))
epsilon = 0.00001

if target < 0 or target >= 1:
    print("Enter a value from 0 (inclusive) to 1 (exclusive).")
else:
    fraction = target
    result = 0.0
    place = 0.5
    digits = ""

    while abs(result - target) >= epsilon:
        fraction *= 2
        bit = int(fraction)
        digits += str(bit)
        fraction -= bit

        result += bit * place
        place /= 2

    if digits == "":
        digits = "0"

    print(f"Binary: 0.{digits}")
    print(f"Decimal value: {result}")
    print(f"Absolute error: {abs(result - target)}")