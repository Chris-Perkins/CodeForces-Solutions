# Description of the problem can be found at http://codeforces.com/problemset/problem/368/B

n, m = map(int, input().split())
a_n = input().split()
a_i = [int(input()) - 1 for _ in range(m)]

s = set()
for i in range(n - 1, -1, -1):
    s.add(a_n[i])
    a_n[i] = len(s)

for i in a_i:
    print(a_n[i])