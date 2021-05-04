from operator import mul
from functools import reduce


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    products = []
    numbers = [int(i) for i in num]
    for j in range(n-k+1):
        products.append(reduce(mul, numbers[j:j+k]))
    print(max(products))
