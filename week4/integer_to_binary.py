number = int(input("Enter an integer: "))

value = abs(number)
remainders = ""

if value == 0:
    binary = "0"
else:
    while value > 0:
        remainder = value % 2
        remainders += str(remainder)
        value //= 2

    binary = remainders[::-1]

if number < 0:
    binary = "-" + binary

print(f"Binary: {binary}")