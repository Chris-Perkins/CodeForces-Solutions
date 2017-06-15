# Description of the problem can be found at http://codeforces.com/problemset/problem/401/C

n, m = map(int, input().split())

if not (m <= 2 * (n + 1) and m >= (n - 1)):
    print(-1)
    quit()
else:
    ma=max(min(m-n,n),0)
    print("1" * (m - n * 2) + "011" * ma + (min(n, m) - ma) * "01" + "0" * (n > m))
        