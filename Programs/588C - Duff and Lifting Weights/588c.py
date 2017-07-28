# Description of the problem can be found at http://codeforces.com/problemset/problem/587/A

n = int(input())
w = map(int, input().split())
m = 1000001
s = [0] * m

for i in w:
    s[i] += 1

ans = 0
z = 0
for i in range(m):
    n_s = s[i]+z
    z = n_s // 2
    ans += n_s % 2

while z > 0:
    ans += z % 2
    z //= 2

print(ans)