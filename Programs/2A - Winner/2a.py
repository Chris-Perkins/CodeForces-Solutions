# Description of the problem can be found at http://codeforces.com/problemset/problem/2/A

n = int(input())

l_k = list()
for _ in range(n):
    l_k.append(input().split())

d_s = {}
for i in range(n):
    k = l_k[i][0]
    s = int(l_k[i][1])
    
    if k not in d_s:
        d_s[k] = int(s)
    else:
        d_s[k] += int(s)

m = max(d_s[x] for x in d_s)

d_s_2 = {}
for i in range(n):
    k = l_k[i][0]
    s = int(l_k[i][1])
    
    if k not in d_s_2:
        d_s_2[k] = int(s)
    else:
        d_s_2[k] += int(s)
        
    if d_s_2[k] >= m and d_s[k] == m:
        print(k)
        quit()