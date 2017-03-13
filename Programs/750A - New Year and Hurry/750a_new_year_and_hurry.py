# Description of the problem can be found at http://codeforces.com/problemset/problem/750/A

n, k = map(int, input().split())
t = 4*60 - k

n_p_c = 0
while t >= 0 and n_p_c <= n:
    n_p_c += 1
    t -= n_p_c* 5
    
print(n_p_c - 1)