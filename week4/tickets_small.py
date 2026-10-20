total_tickets = 10

for alyssa in range(total_tickets + 1):
    for ben in range(total_tickets + 1):
        cindy = total_tickets - alyssa - ben

        if cindy >= 0 and ben == alyssa - 2 and cindy == 2 * alyssa:
            print(f"Alyssa: {alyssa}")
            print(f"Ben: {ben}")
            print(f"Cindy: {cindy}")