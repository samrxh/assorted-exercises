# From Harvard's CS50

# -If n is 1, stop.
# -Otherwise, if n is even, repeat this process on n/2.
# -Otherwise, if n is odd, repeat this process on 3n + 1.
# Write a recursive function collatz(n) that calculates how many steps it
# takes to get to 1 if you start from n and recurse as indicated above.

def collatz(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + collatz(n / 2)
    elif n % 2 == 1:
        return 1 + collatz(3 * n + 1)


while True:
    try:
        number = int(input("Enter a number: "))
        result = collatz(number)
        print(f"It takes {result} step(s) to get from {number} to 1.")
        break
    except ValueError:
        print("Please enter an integer.")
