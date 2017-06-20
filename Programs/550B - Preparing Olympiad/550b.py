# Description of the problem can be found at http://codeforces.com/problemset/problem/550/B

def b_f(l_v, c_v, c_i, l, h, l_p, h_p, x):
    if c_i == len(l_v):
        return 0
    else:
        n_l = l_v[c_i] if not l_p else min(l_v[c_i], l_p)
        n_h = l_v[c_i] if not l_p else max(l_v[c_i], h_p)
        
        return (1 if c_v + l_v[c_i] >= l and 
                     c_v + l_v[c_i] <= h  and
                     n_h - n_l >= x else 0) + (
                     b_f(l_v, c_v, c_i + 1, l, h, l_p, h_p, x) + 
                     b_f(l_v, c_v + l_v[c_i], c_i + 1, l, h, n_l, n_h, x))

n, l, r, x = map(int, input().split())
l_v = list(map(int, input().split()))
print(b_f(l_v, 0, 0, l, r, None, None, x))
