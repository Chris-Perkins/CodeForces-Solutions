# Description of the problem can be found at http://codeforces.com/problemset/problem/514/B

n, x1, y1 = map(int, input().split())

s_s = set()
for _ in range(n):
    x2, y2 = map(int, input().split())
   
    s_s.add((y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else "no slope")
    
print(len(s_s))