# Description of the problem can be found at http://codeforces.com/problemset/problem/804/B

MOD = 1e9 + 7
s = input()

ans = 0
b = 0
for c in s[::-1]:
    if c == 'a':
        ans = (ans + b) % MOD
        b = (2 * b) % MOD
    else:
        b = (b + 1) % MOD

print(int(ans))