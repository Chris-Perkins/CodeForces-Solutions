# Description of the problem can be found at http://codeforces.com/problemset/problem/615/A

n, m = map(int, input().split())
s_s = set()

for _ in range(n):
    s_s.update(list(map(int, input().split()))[1:])
    
if len(s_s) == m:
    print("YES")
else:
    print("NO")