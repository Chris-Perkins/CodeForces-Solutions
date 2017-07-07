# Description of the problem can be found at http://codeforces.com/problemset/problem/322/A

b, g = map(int, input().split())

print(b + g - 1)

for i in range(1, g + 1):
    print("%d %d" % (1, i))

for i in range(2, b + 1):
    print("%d %d" % (i, 1))