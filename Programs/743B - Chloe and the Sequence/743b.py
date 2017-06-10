# Description of the problem can be found at http://codeforces.com/problemset/problem/743/B

n, k = map(int, input().split())

t = 1
while k % 2 == 0:
    t += 1
    k //= 2
print(t)