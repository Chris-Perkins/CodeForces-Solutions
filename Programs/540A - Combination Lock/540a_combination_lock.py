# Description of the problem can be found at http://codeforces.com/problemset/problem/540/A

l = int(input())
o_l = input()
w_l = input()
s = 0

for i in range(l):
    s += min((10 + int(o_l[i]) - int(w_l[i])) % 10, (10 + int(w_l[i]) - int(o_l[i])) % 10)
    
print(s)