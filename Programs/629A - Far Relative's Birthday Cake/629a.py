# Description of the problem can be found at http://codeforces.com/problemset/problem/629/A

def comb(N,k): # from scipy.comb(), but MODIFIED!
    if (k > N) or (N < 0) or (k < 0):
        return 0
    N,k = map(int,(N,k))
    top = N
    val = 1
    while (top > (N-k)):
        val *= top
        top -= 1
    n = 1
    while (n < k+1):
        val //= n
        n += 1
    return val

n = int(input())

a_r = [0] * n
a_c = [0] * n

for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == "C":
            a_r[i] += 1
            a_c[j] += 1

print(sum(comb(a_r[i], 2) + comb(a_c[i], 2) for i in range(n)))