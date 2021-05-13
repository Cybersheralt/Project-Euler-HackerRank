t = int(input().strip())
num = 10**6
primes = [True for i in range(num+4)]
p = 2
answer = [0] * (num + 2)

while p*p <= num+4:
    if primes[p]:
        for j in range(p*2, num+4, p):
            primes[j] = False
    p += 1
primes[0], primes[1] = False, False

for i in range(1, num+1):
    if primes[i]:
        answer[i] = answer[i-1] + i
    else:
        answer[i] = answer[i-1]

for a0 in range(t):
    n = int(input().strip())
    print(answer[n])
