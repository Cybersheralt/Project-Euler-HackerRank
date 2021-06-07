from math import factorial

t = int(input())


def solve(n1, n2):
    return int(factorial(n1+n2) // (factorial(n1) * factorial(n2)))


for _ in range(t):
    n, m = list(map(int, input().split(' ')))
    print(solve(n, m) % 1000000007)
