# Description of the problem can be found at http://codeforces.com/problemset/problem/199/A

f = list([0])

def get_fib(a, b, l):
    if b + a <= l:
        f.append(a + b)
        get_fib(b, b + a, l)
        
def get_seq(i, c_i, c_s, n):
    if c_i == 3 and c_s == n:
        return []
    elif c_i == 3 or c_s > n:
        return None
    else:
        for j in range(i + 1):
            v = get_seq(j, c_i + 1, c_s + f[j], n)
            if v != None:
                v.append(str(f[j]))
                return v
n = int(input())
get_fib(0, 1, n)
v = get_seq(len(f) - 1, 0, 0, n)
if v != None:
    print(" ".join(v))
else:
    print("I'm too stupid to solve this problem")