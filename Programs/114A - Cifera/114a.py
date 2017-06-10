# Description of the problem can be found at http://codeforces.com/problemset/problem/114/A

n = int(input())
k = int(input())

t = -1
while k != 1 and k % n == 0:
    k //= n
    t += 1
if k == 1:
    print("YES\n" + str(t))
else:
    print("NO")