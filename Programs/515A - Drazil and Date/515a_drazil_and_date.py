# Description of the problem can be found at http://codeforces.com/problemset/problem/515/A

a, b, s = map(int, input().split())
if (s - abs(a) - abs(b)) % 2 == 0 and s >= abs(a) + abs(b):
    print("Yes")
else:
    print("No")