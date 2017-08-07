# Description of the problem can be found at http://codeforces.com/problemset/problem/722/B


v = {"a", "e", "i", "o", "u", "y"}
n = int(input())
w = list(map(int, input().split()))
for i in range(n):
    t = 0
    for c in input():
        t += (c.lower() in v)
    if t != w[i]:
        print("NO")
        quit()
print("YES")