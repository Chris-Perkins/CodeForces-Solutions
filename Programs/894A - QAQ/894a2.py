# Description of the problem can be found at http://codeforces.com/problemset/problem/894/A

s = input()
l = len(s)
t = 0
for i in range(l):
    for j in range(i + 1, l):
        for k in range(j + 1, l):
            if s[i] == "Q" and s[j] == "A" and s[k] == "Q":
                t += 1

print(t)