m = 5 * 10**6
lens = [0] * (m+1)
answer = [0]
t = int(input())
inp = [int(input()) for _ in range(t)]
count = 0
longest = 1
maximum = max(inp)


def collatz(n):
    if n < m+1:
        if lens[n] != 0:
            return lens[n]
        else:
            pass
    else:
        pass

    if n == 1:
        return 0
    else:
        if n % 2 == 0:
            result = 1 + collatz(n >> 1)
        else:
            result = 1 + collatz(3*n + 1)

        if n < m+1:
            lens[n] = result
        else:
            pass

        return result


for i in range(1, maximum+1):
    current = collatz(i)
    if current >= count:
        count = current
        longest = i
    answer.append(longest)


for num in inp:
    print(answer[num])
