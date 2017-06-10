# Description of the problem can be found at http://codeforces.com/problemset/problem/701/B

n, m = map(int, input().split())
s_sy = set()
s_sx = set()

for _ in range(m):
    x, y = map(int, input().split())
    
    s_sy.add(y)
    s_sx.add(x)
    
    print(n * n - ((len(s_sx) + len(s_sy)) * n - len(s_sx) * len(s_sy)), end = " ")