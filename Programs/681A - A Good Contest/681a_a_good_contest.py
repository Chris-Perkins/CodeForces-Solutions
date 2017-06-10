# Description of the problem can be found at http://codeforces.com/problemset/problem/681/A
n = int(input())

for _ in range(n):
    s, b, a = input().split()
    if int(b) >= 2400 and int(a) > int(b):
        print("YES")
        quit()
print("NO")