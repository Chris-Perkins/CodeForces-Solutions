# Description of the problem can be found at http://codeforces.com/problemset/problem/525/B

s = list(input())
m = int(input())
s_s = [0] * len(s)

for a in map(int, input().split()):
    s_s[a - 1] += 1

cur = 0
for i in range(len(s) // 2):
    cur += s_s[i]
    if cur & 1:
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

print("".join(s))