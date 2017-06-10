# Description of the problem can be found at http://codeforces.com/problemset/problem/732/A
a, b = map(int, input().split())
i = 1
while 0 != (i * a) % 10 != b:
    i += 1
print(i)