# Description of the problem can be found at http://codeforces.com/problemset/problem/527/A
# originally implemented with recursive function made below, but exceeded recursion depth.
'''
def get_ship_count(a, b):
    if a == b:
        return 1
    if a - b > b:
        return 1 + get_ship_count(a - b, b)
    else:
        return 1 + get_ship_count(b, a - b)
'''

a, b = map(int, input().split())

t = 0
while b != 0:
    t += a // b
    h = a % b
    a = b
    b = h

print(t)