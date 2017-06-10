# Description of the problem can be found at http://codeforces.com/problemset/problem/456/A

n = int(input())
l_p = list()
l_q = list()
for _ in range(n):
    p, q = map(int, input().split())
    l_p.append(p)
    l_q.append(q)
    
l_l = sorted(zip(l_p, l_q))

b_q = 0
p_p = 0
for t in l_l:
    if p_p < t[0] and b_q > t[1]:
        print("Happy Alex")
        quit()
        
    p_p = t[0]
    b_q = max(b_q, t[1])
print("Poor Alex")