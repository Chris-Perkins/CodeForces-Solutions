# Description of the problem can be found at http://codeforces.com/problemset/problem/595/A

r, c = map(int, input().split())

t = 0

for _ in range(r):
    l_w = list(map(int, input().split()))
    
    for i in range(len(l_w) // 2):
        if l_w[i * 2] == 1 or l_w[i * 2 + 1] == 1:
            t += 1

print(t)