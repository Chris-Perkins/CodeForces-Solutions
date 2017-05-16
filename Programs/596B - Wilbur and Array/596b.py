# Description of the problem can be found at http://codeforces.com/problemset/problem/596/B

n = int(input())
l_i = list(map(int, input().split()))

c = 0
t = 0

for i in l_i:
    t += abs(c - i)
    c = i
print(t)