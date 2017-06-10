# Description of the problem can be found at http://codeforces.com/problemset/problem/265/A

p = 0
l_s = input()
l_i = input()

for i in l_i:
    if i == l_s[p]:
        p += 1
        if p == len(l_s):
            break
print(p + 1)