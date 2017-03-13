# Description of the problem can be found at http://codeforces.com/problemset/problem/467/B

# gets the numbers of bits that differ between "a" and "f"
def get_diff(a, f):
    s = 0

    while a != 0 or f != 0:
        a_b = a % 2
        f_b = f % 2
        a //= 2
        f //= 2
        if a_b != f_b:
            s += 1
    
    return s


n, m, k = map(int, input().split())
l = list()

for _ in range(m):
    l.append(int(input()))
f = int(input())

s = 0
for i in l:
    s += 1 if get_diff(i, f) <= k else 0
print(s)