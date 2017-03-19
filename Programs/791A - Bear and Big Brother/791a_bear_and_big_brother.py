# Description of the problem can be found at http://codeforces.com/contest/791/problem/0

a, b = map(int, input().split())
y = 0

while a <= b:
    a *= 3
    b *= 2
    y += 1

print(y)