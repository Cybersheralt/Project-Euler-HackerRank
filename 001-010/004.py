t = int(input().strip())
pals = []
for i in range(100, 1000):
    for j in range(100, 1000):
        numb = i*j
        if len(str(numb)) == 6:
            if (str(numb) == str(numb)[::-1]) and numb not in pals:
                pals.append(numb)
            else:
                pass
        else:
            pass
pals.sort()
for a0 in range(t):
    n = int(input().strip())
    i = 0
    while pals[i] < n:
        i += 1
    print(pals[i-1])
