# Description of the problem can be found at http://codeforces.com/problemset/problem/272/A

n = int(input())
t = sum(list(map(int, input().split())))
    
t_a = 0
for i in range(1, 6):
    if (t + i) % (n + 1) != 1:
        t_a += 1
print(t_a)