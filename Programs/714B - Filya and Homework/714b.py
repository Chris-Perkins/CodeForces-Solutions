# Description of the problem can be found at http://codeforces.com/problemset/problem/714/B

n = int(input())
l_n = list(map(int, input().split()))

h = max(l_n)
l = min(l_n)

for n in l_n:
    if n != h and n!= l:
        if abs(n - h) != abs(n - l):
            print("NO")
            quit()
print("YES")