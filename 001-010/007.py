t = int(input().strip())
num = 104729
primes = [True for i in range(num+1)]
p = 2
answer = []

while p*p <= num+1:
    if primes[p] == True:
        for j in range(p*2, num+1, p):
            primes[j] = False
    p += 1
primes[0], primes[1] = False, False

for i in range(num+1):
    if primes[i]:
        answer.append(i)

for a0 in range(t):
    n = int(input().strip())
    print(answer[n-1])
