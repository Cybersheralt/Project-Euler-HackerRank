t = int(input().strip())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
doubles = [4, 8, 16, 32]
triples = [9, 27]
fives = [25]
for a0 in range(t):
    n = int(input().strip())
    num = 1
    for i in range(1, n+1):
        if i in primes:
            num *= i
        else:
            if i in doubles:
                num *= 2
            else:
                if i in triples:
                    num *= 3
                else:
                    if i in fives:
                        num *= 5
                    else:
                        pass
    print(num)
