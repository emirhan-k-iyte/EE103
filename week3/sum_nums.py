n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Enter zero or a positive integer.")
else:
    total = 0

    for i in range(1, n + 1):
        total += i

    sum_gauss = n * (n + 1) // 2

    print(f"Running sum: {total}")
    print(f"Gauss sum: {sum_gauss}")

    if total == sum_gauss:
        print("My running sum code works correctly")
    else:
        print("My running sum code failed badly")