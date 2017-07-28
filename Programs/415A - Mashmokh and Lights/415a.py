# Description of the problem can be found at http://codeforces.com/problemset/problem/415/A

n, m = map(int, input().split())
l_p = list(map(int, input().split()))

x = [0] * (n + 1)

for b in l_p:
    for i in range(b, n + 1):
        if x[i] == 0:
            x[i] = b
        else:
            break
print(" ".join(str(x) for x in x[1:]))