# Description of the problem can be found at http://codeforces.com/problemset/problem/26/A

n = int(input())
t = [0] * (n + 1)   
for i in range(2, n // 2 + 1):
    if t[i] == 0:
        for j in range(2 * i, n + 1, i):
            t[j] += 1    
print(t.count(2))