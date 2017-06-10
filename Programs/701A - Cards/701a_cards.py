# Description of the problem can be found at http://codeforces.com/problemset/problem/701/A

n = int(input())
l_c = list(map(int, input().split()))
l_i = list()
for i in range(n):
    l_i.append(i + 1)
l_ci = sorted(zip(l_c, l_i))

for i in range(n // 2):
    print("%d %d" % (l_ci[i][1], l_ci[len(l_ci) - 1 - i][1]))