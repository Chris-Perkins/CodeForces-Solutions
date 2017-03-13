# Description of the problem can be found at http://codeforces.com/problemset/problem/621/A

n = int(input())
l_n = list(map(int, input().split()))
l_n.sort()

s = 0
n_o = 0
l_o = -1

for i in range(len(l_n)):
    s += l_n[len(l_n) - 1 - i]
    if l_n[len(l_n) - 1 - i] % 2 == 1:
        l_o = l_n[len(l_n) - 1 - i]
        n_o += 1
        
if n_o % 2 == 1:
     print(s - l_o)
else:
    print(s)