# Description of the problem can be found at http://codeforces.com/problemset/problem/472/B

n, k = map(int, input().split())
l_p = list(map(int, input().split()))
l_p.sort(reverse = True)

i = 0
t = 0
while i < n:
    t += (l_p[i] - 1) * 2
    i += k
print(t)