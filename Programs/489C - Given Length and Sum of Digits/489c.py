# Description of the problem can be found at http://codeforces.com/problemset/problem/489/C

n, s = map(int, input().split())

if n == 1 and s == 0:
    print(0, 0)
elif 9 * n < s or s == 0:
    print(-1, -1)
else:
    r1 = 10 ** (n - 1)
    for i in range(s - 1):
        r1 += 10 ** (i // 9)
    
    r2 = 0
    for i in range(s):
        r2 += 10 ** (n - 1 - i // 9)
    print(r1, r2)