# Description of the problem can be found at http://codeforces.com/problemset/problem/725/A

n = int(input())
s = input()

t_l = 0
t_r = 0

for c in s:
    if c == "<":
        t_l += 1
    else:
        break
for c in s[::-1]:
    if c == '>':
        t_r += 1
    else:
        break
print(t_l + t_r)