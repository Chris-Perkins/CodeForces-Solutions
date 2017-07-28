# Description of the problem can be found at http://codeforces.com/problemset/problem/581/C

n, k = map(int, input().split())
l_s = list(map(int, input().split()))

l_s.sort(key = lambda x: x % 10 if x != 100 else x, reverse = True)

t = 0
r = 0
index = 0
for i in l_s:
    n_i = i
    if i != 100:
        n_i += min(k, 10 - i % 10)
        k -= n_i - i
        r += 100 - n_i
    t += n_i // 10
t += min(r // 10, k // 10)
print(t)