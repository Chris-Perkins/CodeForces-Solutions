# Description of the problem can be found at http://codeforces.com/problemset/problem/598/A
  
t = int(input())

dp = [0] * 30
i = 2
c_i = 1
dp[0] = 1
while c_i < 30:
    dp[c_i] = dp[c_i - 1] + i
    i *= 2
    c_i += 1
    
def b_s(l, h, v):
    if l > h:
        return l - 1
    m = (l + h) // 2
    if 2**m > v:
        return b_s(l, m - 1, v)
    elif 2**m < v:
        return b_s(m + 1, h, v)
    else:
        return m

for _ in range(t):
    s = int(input())
    t_s = b_s(0, len(dp), s)
    print((s*(s + 1)) // 2 - dp[t_s] * 2)