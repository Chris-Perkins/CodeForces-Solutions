# Description of the problem can be found at http://codeforces.com/problemset/problem/313/B

s = input()
n = int(input())

s_f = [0] * len(s)
for i in range(len(s) - 1):
    s_f[i + 1] = s_f[i] + (s[i] == s[i + 1])
s = ""
for _ in range(n):
    l, r = map(int, input().split())
    s += str(s_f[r - 1] - s_f[l - 1]) + "\n"
    
print(s)