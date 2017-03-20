# Description of the problem can be found at http://codeforces.com/problemset/problem/455/A

n = int(input())
l_n = list(map(int, input().split()))
dp = [0]*(10**6)
for n_t in l_n:
    dp[n_t] += 1
for i in range(2, 10**6):
    dp[i] = max(dp[i - 1], dp[i - 2] + dp[i]*i)

print(dp[10**6 - 1])