# Description of the problem can be found at http://codeforces.com/problemset/problem/189/A

n, a, b, c = map(int, input().split())
dp = [0] + [-1e9]*5000

for i in range(1, n + 1):
    dp[i] = max(dp[i - a], dp[i - b], dp[i - c]) + 1

print(dp[n])