# Description of the problem can be found at http://codeforces.com/problemset/problem/604/A

l_m = list(map(int, input().split()))
l_w = list(map(int, input().split()))
l_h = list(map(int, input().split()))

t = 0

for i in range(1, len(l_m) + 1):
    t += max(0.3*500*i, (1 - l_m[i - 1] / 250) * 500 * i - 50 * l_w[i - 1])
print(int(t + l_h[0] * 100 - l_h[1] * 50))