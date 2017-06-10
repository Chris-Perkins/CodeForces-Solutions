# Description of the problem can be found at http://codeforces.com/problemset/problem/549/A

n, m = map(int, input().split())

if n == 1 or m == 1:
    print(0)
    quit()
    
s_f = set(["f", "a", "c", "e"])
t = 0
 
l_p = list()
for i in range(n):
    l_p.append(input())
 
for i in range(n - 1):
    for j in range(m - 1):
        s_s = set([l_p[i][j], l_p[i + 1][j], l_p[i][j + 1], l_p[i + 1][j + 1]])
        if s_s == s_f:
            t += 1
                 
print(t)