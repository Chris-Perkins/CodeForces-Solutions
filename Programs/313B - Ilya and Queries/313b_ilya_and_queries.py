# Description of the problem can be found at http://codeforces.com/problemset/problem/313/B

s = input()

dp = [0]*len(s)
for i in range(1, len(s)):
    dp[i] = dp[i - 1] + (s[i] == s[i - 1])

for _ in range(int(input())):
    l, h = map(int, input().split())
    print(dp[h - 1] - dp[l - 1])