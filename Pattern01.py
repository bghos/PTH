# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

Ntext = sys.stdin.readline().strip()
N = int(Ntext)


# Top cone
for i in range(N):
    print(('H' * (2 * i + 1)).center(2 * N - 1).rjust(2 * N -1 ))
## had to add buffer for N=3 as  -1 and N> 3 as -2
# Top pillars
for i in range(N + 1):
    print(('H' * N).center(2 * N-2).rjust(2 * N-1 ) + ('H' * N).center(2 * N -5 ).rjust(4 * N - 2))

# Middle belt
for i in range((N + 1) // 2):
    print(('H' * N * 5).rjust(N*5 + int(N/2)))
## had to add buffer for N=3 as  -1 and N> 3 as -2
# Bottom pillars
for i in range(N + 1):
    print(('H' * N).center(2 * N-2).rjust(2 * N-1 ) + ('H' * N).center(2 * N -5 ).rjust(4 * N - 2))


# Bottom cone
for i in range(N):
    print(('H' * (2 * (N - i) - 1)).center(2*N*5-1).rjust(2*N-2))