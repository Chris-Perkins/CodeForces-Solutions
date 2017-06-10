# Description of the problem can be found at http://codeforces.com/problemset/problem/43/A

d_n = {}
for i in range(int(input())):
    s = input()
    if s not in d_n:
        d_n[s] = 0
    d_n[s] += 1

inverse = [(value, key) for key, value in d_n.items()]
print(max(inverse)[1])