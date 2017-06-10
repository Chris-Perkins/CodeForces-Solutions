# Description of the problem can be found at http://codeforces.com/problemset/problem/733/A

s_v = set()
s_v.add("A")
s_v.add("E")
s_v.add("I")
s_v.add("O")
s_v.add("U")
s_v.add("Y")

s = input()
p = -1
m = -1

for i in range(len(s)):
    if s[i] in s_v:
        m = max(m, i - p)
        p = i
i += 1
m = max(m, i - p)

print(m)