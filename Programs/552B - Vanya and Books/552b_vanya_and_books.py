# Description of the problem can be found at http://codeforces.com/problemset/problem/552/B

n = int(input())
t = 0
c = 9
i = 1

while n > 0:
    m = min(c, n)
    t += i * m
    n -= m
    i += 1
    c *= 10
    
    
print(t)