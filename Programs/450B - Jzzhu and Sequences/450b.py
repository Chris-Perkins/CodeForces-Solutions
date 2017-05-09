# Description of the problem can be found at http://codeforces.com/problemset/problem/450/B

x, y = map(int, input().split())
n = int(input())

if n % 6 == 1:
    print(x % int(1e9 + 7))
elif n % 6 == 2:
    print(y % int(1e9 + 7))
elif n % 6 == 3:
    print((y - x) % int(1e9 + 7))
elif n % 6 == 4:
    print(-x % int(1e9 + 7))
elif n % 6 == 5:
    print(-y % int(1e9 + 7))
elif n % 6 == 0:
    print((x - y) % int(1e9 + 7))