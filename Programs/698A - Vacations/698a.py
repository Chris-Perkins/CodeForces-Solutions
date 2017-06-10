# Description of the problem can be found at http://codeforces.com/problemset/problem/698/A

n = int(input())
l_n = list(map(int, input().split()))

p = l_n[0]
t = 1 if p == 0 else 0

for i in range(1, n):
    if l_n[i] == p and p != 3:
        l_n[i] = 0
    elif l_n[i] == 3 and p != 3:
        l_n[i] -= p
    if l_n[i] == 0:
        t += 1
    p = l_n[i]

print(t)