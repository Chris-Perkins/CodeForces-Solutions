# Description of the problem can be found at http://codeforces.com/problemset/problem/446/A

n=int(input())

a=list(map(int, input().split()))

pre=[1] * n
suf=[1] * n

for i in range(1, n):
    if a[i] > a[i - 1]:
        pre[i] = pre[i - 1] + 1
for i in range(n - 2, 0, -1):
    if a[i] < a[i + 1]:
        suf[i] = suf[i + 1] + 1

ans=max(pre)

for i in range(0, n):
    if i > 0:
        ans=max(ans, pre[i - 1] + 1)
    if i < n - 1:
        ans = max(ans, suf[i + 1] + 1)
    if i > 0 and i < n - 1 and a[i - 1] <= a[i + 1] - 2:
        ans = max(ans, pre[i - 1] + suf[i + 1] + 1)
print(ans)