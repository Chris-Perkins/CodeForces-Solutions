# Description of the problem can be found at http://codeforces.com/problemset/problem/677/B

n, h, k = map(int, input().split())

l_h = list(map(int, input().split()))

t_h = 0
t_s = 0
m = 0
for (index, c_h) in enumerate(l_h):
    if c_h + t_h > h:
        c_t = (-h + t_h + c_h) // k + (1 if (-h + t_h + c_h) % k != 0 else 0)
        t_s += c_t
        t_h = max(t_h - c_t * k, 0)
        t_h += c_h
    else:    
        t_h += c_h

t_s += t_h // k + (1 if (t_h % k) != 0 else 0)
print(t_s)