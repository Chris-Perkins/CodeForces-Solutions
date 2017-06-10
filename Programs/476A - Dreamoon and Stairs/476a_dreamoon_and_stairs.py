# Description of the problem can be found at http://codeforces.com/problemset/problem/476/A

n, m = map(int, input().split())

for i in range(n // 2  + n % 2, n + 1):
    if i % m == 0:
        print(i)
        quit()
print(-1)