t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    maximum = 1
    while i*i <= n:
        while n % i == 0:
            maximum = i
            n = n // i
        i += 1
    if n > maximum:
        print(n)
    else:
        print(maximum)
