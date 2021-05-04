t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    square_sum = int(n * (n + 1) * (2*n + 1) / 6)
    sum_square = int(n * (n + 1) / 2) ** 2
    print(sum_square - square_sum)
