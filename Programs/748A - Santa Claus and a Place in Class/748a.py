# Description of the problem can be found at http://codeforces.com/problemset/problem/748/A

n, m , k = map(int, input().split())

k -= 1
p = k // 2
p = p // m

print("%d %d %s" % (p + 1, k // 2 - p * m + 1, "R" if k % 2 == 1 else "L"))