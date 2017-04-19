# Description of the problem can be found at http://codeforces.com/problemset/problem/476/B

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
        val /= n
        n += 1
    return val

s = input()
p = 0
m = 0
for c in s:
    if c == "+":
        p += 1
    else:
        m += 1

s = input()
u = 0
for c in s:
    if c == "+":
        p -= 1
    elif c == "-":
        pass
    else:
        u += 1

print(comb(u, p) / 2**u)