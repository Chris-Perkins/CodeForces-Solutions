# Description of the problem can be found at http://codeforces.com/problemset/problem/680/B

n, a = map(int, input().split())
l_c = list(map(int, input().split()))

a -= 1

t = 0
for i in range(n):
    d = abs(a - i)
    
    if a - d < 0 or a + d >= n:
        t += 1 if l_c[i] == 1 else 0
    elif a - d >= 0 and a + d < n:
        t += 1 if l_c[a - d] == l_c[a + d] == 1 else 0

print(t)