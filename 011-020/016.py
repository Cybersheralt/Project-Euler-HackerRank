t = int(input())

for _ in range(t):
    n = int(input())
    num = [int(i) for i in str(2**n)]
    print(sum(num))
