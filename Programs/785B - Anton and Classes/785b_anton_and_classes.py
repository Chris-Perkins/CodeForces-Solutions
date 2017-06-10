# Description of the problem can be found at http://codeforces.com/contest/785/problem/B


l_c = list()
for _ in range(int(input())):
    l_c.append(list(map(int, input().split())))
l_p = list()
for _ in range(int(input())):
    l_p.append(list(map(int, input().split())))
    
max_c = 1
min_c = None
for c in l_c:
    # get max start time, min end time
    max_c = max(max_c, c[0])
    
    if min_c == None:
        min_c = c[1]
    else:
        min_c = min(min_c, c[1])  
    
max_p = 1
min_p = None
for p in l_p:
    max_p = max(max_p, p[0])

    if min_p == None:
        min_p = p[1]
    else:
        min_p = min(min_p, p[1])

print(max(0, max_p - min_c, max_c - min_p))