# Description of the problem can be found at http://codeforces.com/problemset/problem/780/B

n = int(input())
l_p = list(map(int, input().split()))
l_s = list(map(int, input().split()))

def ternary_search(l, h):
    # while we're greater than maximum error
    while (h - l) > 1e-6:
        d = (h - l) / 3
    
        t2 = get_time_to_pos(l + d)
        t3 = get_time_to_pos(h - d)
        
        if t2 < t3:
            h = l + 2 * d
        else:
            l = l + d
    
    return get_time_to_pos((l + h) / 2)


def get_time_to_pos(p):
    return max(abs(p - l_p[i]) / l_s[i] for i in range(n))

h_v = 0
l_v = 1e10
for p in l_p:
    h_v = max(p, h_v)
    l_v = min(p, l_v)
print(ternary_search(l_v, h_v))