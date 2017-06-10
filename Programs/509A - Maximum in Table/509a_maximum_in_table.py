# Description of the problem can be found at http://codeforces.com/problemset/problem/509/A

s = int(input())
table = [[1 for _ in range(s)] for _ in range(s)]

for r in range(1, s):
    for c in range(1, s):
        table[r][c] = table[r - 1][c] + table[r][c - 1]
        
print(table[s - 1][s - 1])