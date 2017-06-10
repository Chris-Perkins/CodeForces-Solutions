# Description of the problem can be found at http://codeforces.com/problemset/problem/447/B

s = input()

k = int(input())
l_n = list(map(int, input().split()))
m = max(l_n)

t = 0
for i in range(len(s)):
    t += (i + 1)*l_n[ord(s[i]) - ord('a')]

print(m * ((len(s) + k) * (len(s) + k + 1) // 2 - len(s)*(len(s) + 1) // 2) + t)