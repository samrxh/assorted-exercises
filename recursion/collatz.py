# From Harvard's CS50

# -If n is 1, stop.
# -Otherwise, if n is even, repeat this process on n/2.
# -Otherwise, if n is odd, repeat this process on 3n + 1.
# Write a recursive function collatz(n) that calculates how many steps it
# takes to get to 1 if you start from n and recurse as indicated above.

def collatz(n):
    steps = 0
    while True:
        if n == 1:
            return steps
        elif n % 2 == 0:
            steps += 1
            n /= 2
        elif n % 2 == 1:
            steps += 1
            n = 3 * n + 1


number = 6
result = collatz(number)
print(f"It takes {result} step(s) to get from {number} to 1.")
