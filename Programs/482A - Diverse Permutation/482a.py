# Description of the problem can be found at http://codeforces.com/problemset/problem/482/A

n, k = map(int, input().split())

l_n = list()

h = n
l = 1
for i in range(n):
    if i < k:
        if i % 2 == 0:
            l_n.append(i // 2 + 1)
            l = i // 2 + 1
        else:
            l_n.append(n - i // 2)
            h = n - i // 2
    else:
        if i % 2 == 1:
            l_n.extend(l + x for x in range(1, n + 1 - i))
        if i % 2 == 0:
            l_n.extend(h - x for x in range(1, n + 1 - i))
        break
print(" ".join(str(x) for x in l_n))