# Description of the problem can be found at http://codeforces.com/problemset/problem/651/B

n = int(input())
l_p = list(map(int, input().split()))

d_p = {}

for p in l_p:
    if p not in d_p:
        d_p[p] = 1
    else:
        d_p[p] += 1
        
t = 0

while len(d_p) != 0:
    t += len(d_p) - 1
    
    s_k = set()
    
    for k in d_p:
        d_p[k] -= 1
        s_k.add(k)
        
    for k in s_k:
        if d_p[k] == 0:
            del d_p[k]
            
print(t)