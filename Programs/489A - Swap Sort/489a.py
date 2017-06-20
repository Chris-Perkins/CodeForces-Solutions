# Description of the problem can be found at http://codeforces.com/problemset/problem/489/A

n = int(input())

l_v = list(map(int, input().split()))

sa = sorted(l_v)
ans = []
for i in range(n):
    if l_v[i] != sa[i]:
        p = l_v[i:].index(sa[i]) + i
        l_v[i], l_v[p] = l_v[p], l_v[i]
        ans.append([i, p])

print(len(ans))
for a in ans:
    print(" ".join(str(x) for x in a))