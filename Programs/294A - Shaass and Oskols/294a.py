# Description of the problem can be found at http://codeforces.com/problemset/problem/294/A

n = int(input())
l_w = list(map(int, input().split()))

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x - 2 >= 0:
        l_w[x - 2] += y - 1
    if x != n:
        l_w[x] += l_w[x - 1] - y
    
    l_w[x - 1] = 0
    
print("\n".join(str(x) for x in l_w))