t = int(input())


def factor(number):
    factors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.append(i)
            new = number // i
            if new != i:
                factors.append(new)

    return factors


for _ in range(t):
    n = int(input())
    j = 1
    while True:
        if j % 2 == 0:
            numb = len(factor(j / 2)) * len(factor(j + 1))
        else:
            numb = len(factor(j)) * len(factor((j + 1) / 2))

        if numb > n:
            print(int(j * (j + 1) / 2))
            break
        else:
            j += 1
