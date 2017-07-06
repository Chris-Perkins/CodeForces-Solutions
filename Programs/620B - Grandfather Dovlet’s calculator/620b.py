# Description of the problem can be found at http://codeforces.com/problemset/problem/620/B

d = list([6, 2, 5, 5, 4, 5, 6, 3, 7, 6])

a, b = map(int, input().split())
nums = str(list(range(a, b+1)))

r = 0
for i in range(len(d)):
    r += d[i] * nums.count(str(i))
print(r)