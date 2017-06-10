# Description of the problem can be found at http://codeforces.com/problemset/problem/381/A

n = int(input())
l_n = list(map(int, input().split()))

p1 = 0
p2 = 0
l = 0
r = n - 1
p = True
while l <= r:
    if p:
        if l_n[l] > l_n[r]:
            p1 += l_n[l]
            l += 1
        else:
            p1 += l_n[r]
            r -= 1
    else:
        if l_n[l] > l_n[r]:
            p2 += l_n[l]
            l += 1
        else:
            p2 += l_n[r]
            r -= 1
    
    p = not p
    
print("%d %d" % (p1, p2))