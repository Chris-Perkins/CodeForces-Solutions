# Description of the problem can be found at http://codeforces.com/problemset/problem/705/B

n = int(input())

c = 1
for i in list(map(int, input().split())):
    c += i - 1
    print(c % 2 + 1)