# Description of the problem can be found at http://codeforces.com/problemset/problem/746/A

l = int(input())
a = int(input())
p = int(input())

m = min(l, a // 2, p // 4)
print(sum([m, m * 2, m * 4]))