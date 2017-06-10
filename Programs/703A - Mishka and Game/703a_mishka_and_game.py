# Description of the problem can be found at http://codeforces.com/problemset/problem/703/A

n = int(input())
t = 0

for _ in range(n):
    i, j = map(int, input().split())
    
    if i < j:
        t -= 1
    if i > j:
        t += 1

if t > 0:
    print("Mishka")
elif t < 0:
    print("Chris")
else:
    print("Friendship is magic!^^")