# Description of the problem can be found at http://codeforces.com/problemset/problem/545/B

s = input()
t = input()

l_d = list()

c = 0
for i in range(len(s)):
    if s[i] != t[i] and c % 2 == 0:
        l_d.append("0" if "0" == s[i] else "1")
        c += 1
    elif s[i] != t[i]:
        c += 1
        l_d.append("1" if "0" == s[i] else "0")
    else:
        l_d.append("1")
        
if c % 2 == 1:
    print("impossible")
else:
    print("".join(l_d))
        