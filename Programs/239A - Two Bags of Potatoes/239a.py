# Description of the problem can be found at http://codeforces.com/problemset/problem/239/A

y, k, n = map(int, input().split())

a = k - y % k

if y + a <= n:
    if a == 0:
        print(" ".join(str(x) for x in [(t + 1) * k for t in range((n - y) // k)]))
    else:
        print(" ".join(str(x) for x in [a + t * k for t in range((n - y) // k + 1) if a + t * k + y <= n]))
else:
    print(-1)