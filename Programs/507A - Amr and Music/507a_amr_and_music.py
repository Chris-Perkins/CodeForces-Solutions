# Description of the problem can be found at http://codeforces.com/problemset/problem/507/A

n, k = map(int, input().split())

a = [0]*n
d = list(map(int, input().split()))

for i in range(n):
    a[i] = i + 1

s = sorted(zip(d, a))


l_o = list()
i = 0
while i < len(s) and k - s[i][0] >= 0:
    k -= s[i][0]
    l_o.append(s[i][1])
    i += 1 

print(i)
for o in l_o:
    print(o, end = " ")