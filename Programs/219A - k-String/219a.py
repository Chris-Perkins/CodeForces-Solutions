# Description of the problem can be found at http://codeforces.com/problemset/problem/219/A

n = int(input())

d_c = {}
s = input()

for c in s:
    if c not in d_c:
        d_c[c] = 1
    else:
        d_c[c] += 1


ans = ""
for c in d_c:
    if d_c[c] % n != 0:
        print("-1")
        quit()
    else:
        ans = ans + c * (d_c[c] // n)
        
print(ans * n) 