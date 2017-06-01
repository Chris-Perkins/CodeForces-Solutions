# Description of the problem can be found at http://codeforces.com/problemset/problem/682/B

n = int(input())

l_n = list(map(int, input().split()))
l_n.sort()

c = 1

for n in l_n:
    if c <= n:
        c += 1

print(c)