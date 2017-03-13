# Description of the problem can be found at http://codeforces.com/problemset/problem/327/A

n = int(input())
l = list(map(int, input().split()))

m = -1
s = 0

for i in range(n):
    s += 1 if l[i] == 0 else -1
    
    if s > m:
        m = s
    
    if s <= 0:
        s = 0
        c_l = 0

print(sum(l) + m)