# Description of the problem can be found at http://codeforces.com/problemset/problem/515/C

n = int(input())

s = input()

a_n = [0]*10

for c in s:
    if c == '2':
        a_n[2] += 1
    elif c == '3':
        a_n[3] += 1
    elif c == '4':
        a_n[2] += 2
        a_n[3] += 1
    elif c == '5':
        a_n[5] += 1
    elif c == '6':
        a_n[5] += 1
        a_n[3] += 1
    elif c == '7':
        a_n[7] += 1
    elif c == '8':
        a_n[2] += 3
        a_n[7] += 1
    elif c == '9':
        a_n[3] += 2
        a_n[2] += 1
        a_n[7] += 1

for i in range(0, 9):
    while a_n[9 - i] > 0:
        print(9 - i, end = "")
        a_n[9 - i] -= 1