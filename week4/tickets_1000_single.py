from time import perf_counter

total_tickets = 1000
solution = ""
start = perf_counter()

for alyssa in range(total_tickets + 1):
    ben = alyssa - 20
    cindy = 2 * alyssa

    if ben >= 0 and alyssa + ben + cindy == total_tickets:
        solution = f"Alyssa: {alyssa}, Ben: {ben}, Cindy: {cindy}"

elapsed = perf_counter() - start

print(solution)
print(f"Elapsed time: {elapsed:.6f} seconds")