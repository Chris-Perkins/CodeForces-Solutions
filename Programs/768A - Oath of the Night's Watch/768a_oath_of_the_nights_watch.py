# Description of the problem can be found at http://codeforces.com/problemset/problem/768/A

n  = int(input())
l_s = list(map(int, input().split()))

t = 0
l = min(l_s)
m = max(l_s)

for s in l_s:
    if s != l and s!= m:
        t += 1
        
print(t)