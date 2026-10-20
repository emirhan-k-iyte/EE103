from time import perf_counter

total_tickets = 1000
solution = ""
start = perf_counter()

for alyssa in range(total_tickets + 1):
    for ben in range(total_tickets + 1):
        cindy = total_tickets - alyssa - ben

        if cindy >= 0 and ben == alyssa - 20 and cindy == 2 * alyssa:
            solution = f"Alyssa: {alyssa}, Ben: {ben}, Cindy: {cindy}"

elapsed = perf_counter() - start

print(solution)
print(f"Elapsed time: {elapsed:.6f} seconds")