# Description of the problem can be found at http://codeforces.com/problemset/problem/721/A

_ = input()
s = input()

t = 0
l_t = list()

for c in s:
    if c == "B":
        t += 1
    else:
        if t != 0:
            l_t.append(str(t))
        t = 0

if t != 0:
    l_t.append(str(t))

print(len(l_t))
print(" ".join(l_t))