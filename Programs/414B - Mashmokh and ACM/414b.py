# Description of the problem can be found at http://codeforces.com/problemset/problem/414/B

n,k = map(int,input().split())
n += 1
k += 1
dp = [[0] * n for _ in range(13)]
s = 0
M = 1000000007
f = [1]
for i in range(1,4500):
	f.append(f[-1] * i % M)
def C(n, k):
	if k>n:
		return 0
	return  f[n] * pow(f[k] * f[n - k] %M , M - 2, M) % M

for i in range(1, 12):
	for j in range(1, n):
		if i == 1:
			dp[i][j] = 1
		for t in range(j * 2, n, j):
			dp[i + 1][t] = (dp[i + 1][t] + dp[i][j]) % M
		s = (s + C(k - 2, i - 1) * dp[i][j] % M) % M


print(s)