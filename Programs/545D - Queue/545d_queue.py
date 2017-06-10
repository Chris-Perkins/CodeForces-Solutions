# Description of the problem can be found at http://codeforces.com/problemset/problem/545/D

n = int(input())
l_n = list(map(int, input().split()))
l_n.sort()

t = 0
n = 0

for t_n in l_n:
    if t <= t_n:
        t += t_n
        n += 1
print(n)