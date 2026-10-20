fraction = float(input("Enter a fraction (0 <= F < 1): "))
max_bits = 20

if fraction < 0 or fraction >= 1:
    print("Enter a value from 0 (inclusive) to 1 (exclusive).")
else:
    digits = ""

    while fraction > 0 and len(digits) < max_bits:
        fraction *= 2
        bit = int(fraction)
        digits += str(bit)
        fraction -= bit

    if digits == "":
        digits = "0"

    print(f"Binary: 0.{digits}")

    if fraction > 0:
        print("Precision limit reached; result is approximate.")