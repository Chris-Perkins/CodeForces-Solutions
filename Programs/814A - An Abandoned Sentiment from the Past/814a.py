# Description of the problem can be found at http://codeforces.com/problemset/problem/814/A

n, k = map(int, input().split())

l_n = list(map(int, input().split()))
l_r = list(map(int, input().split()))
l_r.sort(reverse = True)

c_r = 0
for i in range(len(l_n)):
    if l_n[i] == 0:
        l_n[i] = l_r[c_r]
        c_r += 1

l_c = l_n.copy()
l_c.sort()

print("Yes" if l_n != l_c else "No")