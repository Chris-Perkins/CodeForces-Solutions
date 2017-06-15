# Description of the problem can be found at http://codeforces.com/problemset/problem/765/A

n = int(input())
s = input()

d = {}
d[s] = 0

for _ in range(n):
    x, y = input().split("->")
    
    if x == s:
        d[s] -= 1
    elif y == s:
        d[s] += 1
        
print("home" if d[s] == 0 else "contest")