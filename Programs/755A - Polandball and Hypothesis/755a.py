# Description of the problem can be fund at http://codeforces.com/problemset/problem/755/A

n = int(input())

if n > 2:
    print(n - 2)
else:
    if n == 2:
        print(4)
    else:
        print(8)