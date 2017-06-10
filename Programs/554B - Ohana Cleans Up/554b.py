# Description of the problem can be found at http://codeforces.com/problemset/problem/554/B

l_s = list(input() for _ in range(int(input())))
m = 0
for i in l_s:
    m = max(m, l_s.count(i))
print(m)