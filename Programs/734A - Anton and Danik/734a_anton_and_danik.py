# Description of the problem can be found at http://codeforces.com/problemset/problem/734/A

_ = input()
l = input()

A = 0
D = 0

for c in l:
    if c == "A":
        A += 1
    else:
        D += 1

if A > D:
    print("Anton")
elif D > A:
    print("Danik")
else:
    print("Friendship")