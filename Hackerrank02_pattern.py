N = 5

# Top cone
for i in range(N):
    print(('H' * (2 * i + 1)).center(2 * N - 1).rjust(4 * N - 3))

# Top pillars
for i in range(N + 1):
    print(('H' * N).center(2 * N - 1).rjust(4 * N - 3) + ('H' * N).center(2 * N - 1).rjust(4 * N - 3))

# Middle belt
for i in range((N + 1) // 2):
    print(('H' * (5 * N)).center(4 * N - 3))

# Bottom pillars
for i in range(N + 1):
    print(('H' * N).center(2 * N - 1).rjust(4 * N - 3) + ('H' * N).center(2 * N - 1).rjust(4 * N - 3))

# Bottom cone
for i in range(N):
    print(('H' * (2 * (N - i) - 1)).center(2 * N - 1).rjust(2 * N - 3))