# Description of the problem can be found at http://codeforces.com/problemset/problem/552/A

n = int(input())

t = 0
for _ in range(n):
    l_c = list(map(int, input().split()))
    t += (abs(l_c[0] - l_c[2]) + 1) * (abs(l_c[1] - l_c[3]) + 1)
    
print(t)