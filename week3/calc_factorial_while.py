n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    i = 1

    while i <= n:
        factorial *= i
        i += 1

    print(f"{n}! = {factorial}")