# Description of the problem can be found at http://codeforces.com/problemset/problem/731/A

s = input()
p_c = 'a'
t = 0

for c in s:
    t += min(abs(ord(c) - ord(p_c)), 26 - abs(ord(c) - ord(p_c)))
    p_c = c
    
print(t)