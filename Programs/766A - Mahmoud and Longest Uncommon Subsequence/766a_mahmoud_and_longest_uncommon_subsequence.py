# Description of the problem can be found at http://codeforces.com/problemset/problem/766/A

a = input()
b = input()

if len(a) > len(b):
    print(len(a))
elif len(a) < len(b):
    print(len(b))
else:
    print(len(a) if not a.__eq__(b) else -1)