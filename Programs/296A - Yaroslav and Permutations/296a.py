# Description of the problem can be found at http://codeforces.com/problemset/problem/296/A

m = 0
a = [0] * 1001

n = int(input())

for i in map(int, input().split()):
    a[i] += 1

    if a[i] > m:
        m = a[i]

if m > n // 2 + (1 if n % 2 == 1 else 0):
    print("NO")
else:
    print("YES")