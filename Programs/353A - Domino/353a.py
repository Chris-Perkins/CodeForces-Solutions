# Description of the problem can be found at http://codeforces.com/problemset/problem/353/A

n = int(input())

s_h = False
s_l = 0
s_r = 0
for _ in range(n):
    x, y = map(int, input().split())
    
    if x % 2 != y % 2:
        s_h = True
    s_l += x
    s_r += y

if ((s_l) % 2 == 1 and (s_r) % 2 == 1 and s_h):
    print(1)
elif (s_l % 2 == 0 == s_r % 2):
    print(0)
else:
    print(-1)   