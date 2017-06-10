# Description of the problem can be found at http://codeforces.com/problemset/problem/557/A

n = int(input())

l_lm = list()
for _ in range(3):
    l_lm.append(list(map(int, input().split())))

n += - l_lm[0][0] - l_lm[1][0] - l_lm[2][0]
l_t = list([l_lm[0][0], l_lm[1][0], l_lm[2][0]])


for i in range(3):
    l_t[i] += min(n, l_lm[i][1] - l_lm[i][0])
    n -= min(n, l_lm[i][1] - l_lm[i][0])

print(" ".join(str(x) for x in l_t))