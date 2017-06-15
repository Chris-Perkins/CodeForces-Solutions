# Description of the problem can be found at http://codeforces.com/problemset/problem/719/B

n = int(input())
s = input()
r = 0
r1 = 0
b = 0
b1 = 0
for i in range(n) :
    if i % 2 == 0:
        if s[i] != 'r':
            r = r + 1
        else:
            b1=b1+1
    else :
        if s[i] != 'b':
            b = b + 1
        else :
            r1 = r1 + 1
print(min(max(r, b), max(r1, b1)))