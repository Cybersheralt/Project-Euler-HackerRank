
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = (n-1) // 3
    b = (n-1) // 5
    ab = (n-1) // 15
    print(int(3 * (a * (a+1)) + 5 * (b * (b+1)) - 15 * (ab * (ab+1)) >> 1))
