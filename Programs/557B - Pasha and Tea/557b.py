# Description of the problem can be found at http://codeforces.com/problemset/problem/557/B

n, w = map(int, input().split())
l_t = list(map(int, input().split()))
l_t.sort()
t_a = min(w / (3 * n), l_t[0], l_t[n] / 2)
print(t_a * n * 3)