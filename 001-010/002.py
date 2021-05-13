t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fib = [0, 2]
    while fib[-1] <= n:
        fib.append(fib[-1]*4 + fib[-2])
    print(sum(fib[:-1]))
