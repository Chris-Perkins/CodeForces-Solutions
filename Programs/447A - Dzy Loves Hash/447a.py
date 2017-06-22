# Description of the problem can be found at http://codeforces.com/problemset/problem/447/A

p, n = map(int, input().split())
d = {}

for i in range(n):
    x = int(input()) % p
    
    if x in d:
        print(i + 1)
        quit()
    d[x] = 1
        
print(-1)