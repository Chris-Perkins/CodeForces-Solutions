# Description of the problem can be found at http://codeforces.com/contest/787/problem/B

n, m = map(int, input().split())
l_g = list(list(map(int, input().split())) for i in range(m))

for g in l_g:
    s = set()
    b = False
    
    for i in range(1, len(g)):
        if -g[i] not in s:
            s.add(g[i])
        else:
            b = True
            break
    
    if not b:
        print("YES")
        quit()
print("NO")