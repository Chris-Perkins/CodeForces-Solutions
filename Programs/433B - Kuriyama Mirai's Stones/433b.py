# Description of the problem can be found at http://codeforces.com/problemset/problem/433/B

n = int(input())

l_n = list(map(int, input().split()))
l_n_s = l_n.copy()
l_n_s.sort()

l_s = list()
l_s_s = list()

l_s.append(l_n[0])
l_s_s.append(l_n_s[0])

for i in range(1, n):
    l_s.append(l_s[i - 1] + l_n[i])
    l_s_s.append(l_s_s[i - 1] + l_n_s[i])
    
for _ in range(int(input())):
    t, l, r = map(int, input().split())
    
    if t == 1:
        if l == 1:
            print(l_s[r - 1])
        else:
            print(l_s[r - 1] - l_s[l - 2])
    else:
        if l == 1:
            print(l_s_s[r - 1])
        else:
            print(l_s_s[r - 1] - l_s_s[l - 2])