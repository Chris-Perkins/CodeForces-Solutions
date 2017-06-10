# Description of the problem can be found at http://codeforces.com/problemset/problem/659/C

n, m = map(int, input().split())
s_t = set(map(int, input().split()))
s_b = set()

i = 1
while m >= i:
    if i not in s_t:
        s_b.add(i)
        m -= i
    i += 1
    
print(len(s_b))
print(" ".join(str(x) for x in s_b))