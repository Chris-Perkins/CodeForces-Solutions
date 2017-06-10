# Description of the problem can be found at http://codeforces.com/problemset/problem/556/B

n = int(input())
l_p = list(map(int, input().split()))

t = -l_p[0] % n

for i in range(n):
    if (l_p[i] + (-1 if i % 2 == 1 else 1)*t) % n != i:
        print("NO")
        quit()
        
print("YES")