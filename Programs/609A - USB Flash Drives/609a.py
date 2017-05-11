# Description of the problem can be found at http://codeforces.com/problemset/problem/609/A

n = int(input())
s = int(input())

l_d = list()
for _ in range(n):
    l_d.append(int(input()))
l_d.sort(reverse=True)

c = 0
t = 0
while s > c and t < n:
    c += l_d[t]
    t += 1

print(t)