# Description of the problem can be found at http://codeforces.com/problemset/problem/115/A

import sys
sys.setrecursionlimit(2500)

class graph:
    m = None
    d = {}
    
    def __init__(self, n):
        self.m = [0 for _ in range(n + 1)]
    
    def add_edge(self, a, b):
        self.m[a] = b
    
    def get_depth(self, a):
        if a == -1:
            return 0
        
        if a not in self.d:
            self.d[a] = 1 + self.get_depth(self.m[a])
        
        return self.d[a]


n = int(input())
g = graph(n)

for p in range(n):
    g.add_edge(p + 1, int(input()))

t = 0
for i in range(1, n + 1):
    t = max(t, g.get_depth(i))

print(t)