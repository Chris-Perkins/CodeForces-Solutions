# Description of the problem can be found at http://codeforces.com/problemset/problem/713/A

from collections import defaultdict
from sys import stdin
from sys import stdout

n = int(stdin.readline())

d = defaultdict(int)        
for _ in range(n):
    s, x = stdin.readline().split()
    y = "".join(["1" if c in ["1", "3", "5", "7", "9"] else "0" for c in x]).zfill(18)
    
    if s == "+": 
        d[y] += 1
    elif s == "-": 
        d[y] -= 1
    else: 
        stdout.write(str(d[y]) + '\n')