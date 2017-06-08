# Description of the problem can be found at http://codeforces.com/problemset/problem/611/B

a, b = map(int, input().split())
ans = 0

full = 0
for mp in range(100):
    full += 2 ** mp
    for zp in range(mp):
        curr = full - 2 ** zp
        if a <= curr <= b:
            ans += 1
print(ans)