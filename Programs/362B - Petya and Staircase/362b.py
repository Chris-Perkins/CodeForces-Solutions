# Description of the problem can be found at http://codeforces.com/problemset/problem/362/B

n, m = map(int, input().split())

if m == 0:
    print("YES")
    quit()

l_d = list(map(int, input().split()))
l_d.sort()
if l_d[0] == 1 or l_d[len(l_d) - 1] == n:
    print("NO")
    quit()

c = 0
p = -1
for d in l_d:
    if d == p + 1:
        c += 1
    else:
        c = 1
    p = d
    
    if c == 3:
        print("NO")
        quit()
print("YES")