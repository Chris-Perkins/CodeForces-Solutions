# Description of the problem can be found at http://codeforces.com/problemset/problem/709/A

n, b, d = map(int, input().split())
l_o = list(map(int, input().split()))

t = 0
t_o = 0
for o in l_o:
    if o <= b:
        t += o
    if t > d:
        t_o += 1
        t = 0
        
print(t_o)