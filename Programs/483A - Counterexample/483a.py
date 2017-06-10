# Description of the problem can be found at http://codeforces.com/problemset/problem/483/A

l, r = map(int, input().split())

if l % 2 ==  1:
    l += 1

if r < l + 2:
    print(-1)
else:
    print("%d %d %d" % (l, l + 1, l + 2))