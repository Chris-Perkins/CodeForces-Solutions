# Description of the problem can be found at http://codeforces.com/problemset/problem/611/A

s = input().split()
x = int(s[0])

if s[2][0] == "w":
    if x >= 5 and x < 7:
        print(52 + 1)
    else:
        print(52)
else:
    if x <= 29:
        print(12)
    elif x == 30:
        print(11)
    else:
        print(7)
    