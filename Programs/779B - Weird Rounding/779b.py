# Description of the problem can be found at http://codeforces.com/problemset/problem/779/B

n, k = input().split()
k = int(k)

n_z = 0
d = 0
for i in range(len(n)):
    if n[len(n) - i - 1] == "0":
        n_z += 1
        if n_z == k:
            print(d)
            quit()
    else:
        d += 1
print(len(n) - 1)