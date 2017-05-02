# Description of the problem can be found at http://codeforces.com/problemset/problem/439/B

n, x = map(int, input().split())
l_c = list(map(int, input().split()))
l_c.sort()

t = 0
for i in range(len(l_c)):
    t += max(1, x - i) * l_c[i]
    
print(t) 