# Description of the problem can be found at http://codeforces.com/problemset/problem/746/B

n = int(input())
s = input()
s_o = ["" for _ in range(len(s))] 

m = len(s) / 2
c = 0
if len(s) % 2 == 1:
    s_o[len(s) // 2] = s[0]
    c = 1

l = (len(s) - c) // 2 - 1
h = (len(s) - c) // 2 + (1 if len(s) % 2 == 1 else 0)

while l != -1 or h != len(s):
    if m - l <= h - m:
        s_o[l] = s[c]
        l -= 1
    else:
        s_o[h] = s[c]
        h += 1
    c += 1
    
s_o.reverse()
print("".join(s_o))