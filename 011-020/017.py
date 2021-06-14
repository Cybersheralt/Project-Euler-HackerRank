one = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
       '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
tens = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen',
        '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen',
        '19': 'Nineteen', '2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty',
        '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'}
endings = {'0': '', '1': 'Thousand', '2': 'Million', '3': 'Billion', '4': 'Trillion'}


def solution_for_3(s):
    ans = ''
    if s[0] != '0':
        ans += one[s[0]] + ' Hundred '

    if (s[1] != '0') and (s[1] != '1'):
        ans += tens[s[1]] + ' '

    if s[1] == '1':
        ans += tens[s[1:]] + ' '

    if (s[1] != '1') and (s[2] != '0'):
        ans += one[s[2]] + ' '
    return ans


def general(n):
    ans = ''
    n = '0' * (3 - len(n) % 3) + n
    i = 0
    while i < len(n)//3:
        if int(n[0 + (3*i):3 + (3*i)]) == 0:
            pass
        else:
            ans += solution_for_3(n[0 + (3*i):3 + (3*i)]) + endings[str(len(n)//3 - i - 1)] + ' '
        i += 1
    return ans


t = int(input())
for _ in range(t):
    num = input()
    if int(num) == 0:
        answer = one['0']
    else:
        answer = general(num)
    print(answer.rstrip(' '))
