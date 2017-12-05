# Description of the problem can be found at http://codeforces.com/problemset/problem/894/A

s = input()

l_q = [0 for _ in range(len(s))]
for (i, c) in enumerate(s):
    if c == "Q":
        l_q[i] += 1
    l_q[i] += 0 if i == 0 else l_q[i - 1]

t = 0
for (i, c) in enumerate(s):
    if c == "A" and i > 0:
        t += (l_q[len(l_q) - 1] - l_q[i - 1]) * l_q[i - 1]

print(t) 