# Description of the problem can be found at http://codeforces.com/problemset/problem/463/B

n = int(input())
l_h = list([0])
l_h.extend(list(map(int, input().split())))

e = 0
t = 0
for i in range(1, len(l_h)):
    e += l_h[i - 1] - l_h[i]
    
    if e < 0:
        t += -e
        e = 0
        
print(t)